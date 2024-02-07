### Health Management APP
from dotenv import load_dotenv

load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type, #Multipurpose Internet Mail Extensions (MIME)
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    


st.set_page_config(page_title="Consumer Awareness App")

st.header("Consumer Awareness App")
input=st.text_input("wish to know something else? ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Sumbit to get calorie information and interdient descrpition")

input_prompt="""
As an expert nutritionist, 
your task is to analyze a food image and provide the following information in the specified format:
\n1.Calculate the total calories of the food items.
\n2.Provide details of each food item with their respective calorie intake.
\nExample format: 
Item 1 - 100 calories
Item 2 - 150 calories\n...\n
Additionally, you are also an expert in recognizing ingredients used in packaged food items. For each ingredient, you need to list its effect on human health and potential side effects  and the common terms of each ingrdient in the format mentioned above.\nPlease provide the required information based on the given food image.
and also give an score out of 5 based on the ingreidents and thier overall effect on health
"""
if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)

