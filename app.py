import streamlit as st
from PIL import Image, UnidentifiedImageError
import pytesseract
import pickle
import pandas as pd
import os
import google.generativeai as genai
import sqlite3
from dotenv import load_dotenv
import io
import google.auth
# Load environment variables
load_dotenv()
# OCR functionality
def ocr_interface():
    st.title("OCR with Streamlit")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button('Perform OCR'):
            extracted_text = pytesseract.image_to_string(image)
            st.write("Extracted Text:")
            st.write(extracted_text)

# Product recommendation functionality
def product_recommendation_interface():
    st.title("Product Recommendation")

    product_dict = pickle.load(open("product_dict.pkl", "rb"))
    products = pd.DataFrame(product_dict)
    similarity = pickle.load(open("similarity.pkl", "rb"))
    unique_brands = products['Brand'].unique()

    selected_brand_name = st.selectbox('Select brand to check out products', unique_brands)

    if st.button('RECOMMEND'):
        product_index = products[products['Brand'] == selected_brand_name].index[0]
        distances = similarity[product_index]
        product_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        for i in product_list:
            st.write(f"Brand: {products.iloc[i[0]].Brand}")
            st.write(f"Label: {products.iloc[i[0]].Label}")
            st.write(f"Ingredients: {products.iloc[i[0]].Ingredients}")
            st.write('-' * 50)

# SQLite database search functionality
def sqlite_search_interface():
    st.title("SQLite Database Search")

    ingredient = st.text_input("Enter the ingredient to search for:")

    if st.button("Search"):
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute("SELECT NAME, BRAND FROM COSMETIC_PRODUCT WHERE Ingredients LIKE ?", ('%' + ingredient + '%',))
        rows = c.fetchall()
        conn.close()

        if rows:
            st.write("Results found:")
            for row in rows:
                st.write(row)
        else:
            st.write("No results found.")

# Gemini model response functionality
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
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

def gemino_response_interface():
    st.title("Gemini Model Response")

    input_prompt = """
    As an expert nutritionist, 
    your task is to analyze a food image and provide the following information in the specified format:
    \n1. Calculate the total calories of the food items.
    \n2. Provide details of each food item with their respective calorie intake.
    \nExample format: 
    Item 1 - 100 calories
    Item 2 - 150 calories\n...\n
    Additionally, you are also an expert in recognizing ingredients used in packaged food items. For each ingredient, you need to list its effect on human health and potential side effects and the common terms of each ingredient in the format mentioned above.
    \nPlease provide the required information based on the given food image.
    and also give an score out of 5 based on the ingredients and their overall effect on health
    """
    
    input_gemino = st.text_input("Wish to know something else? ", key="input_gemino")
    uploaded_file_gemino = st.file_uploader("Choose an image for Gemini...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file_gemino is not None:
        image_gemino = Image.open(uploaded_file_gemino)
        st.image(image_gemino, caption="Uploaded Image for Gemini.", use_column_width=True)
    
    submit_gemino = st.button("Submit to get calorie information and ingredient description")

    if submit_gemino:
        image_data = input_image_setup(uploaded_file_gemino)
        response = get_gemini_repsonse(input_gemino, image_data, input_prompt)
        st.subheader("The Response is")
        st.write(response)


# Main function to call individual interfaces based on user choice
def main():
    st.sidebar.title("Choose Functionality")
    option = st.sidebar.selectbox('Select:', ['OCR', 'Product Recommendation', 'SQLite Search', 'Gemino Response'])

    if option == 'OCR':
        ocr_interface()
    elif option == 'Product Recommendation':
        product_recommendation_interface()
    elif option == 'SQLite Search':
        sqlite_search_interface()
    elif option == 'Gemini Response':
        gemino_response_interface()

if __name__ == "__main__":
    main()

#FLASK CODE



import streamlit as st
from PIL import Image, UnidentifiedImageError
import pytesseract
import pickle
import pandas as pd
import os
import google.generativeai as genai
import sqlite3
from dotenv import load_dotenv
import io
import google.auth
# Load environment variables
load_dotenv()
# OCR functionality
def ocr_interface():
    st.title("OCR with Streamlit")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button('Perform OCR'):
            extracted_text = pytesseract.image_to_string(image)
            st.write("Extracted Text:")
            st.write(extracted_text)

# Product recommendation functionality
def product_recommendation_interface():
    st.title("Product Recommendation")

    product_dict = pickle.load(open("product_dict.pkl", "rb"))
    products = pd.DataFrame(product_dict)
    similarity = pickle.load(open("similarity.pkl", "rb"))
    unique_brands = products['Brand'].unique()

    selected_brand_name = st.selectbox('Select brand to check out products', unique_brands)

    if st.button('RECOMMEND'):
        product_index = products[products['Brand'] == selected_brand_name].index[0]
        distances = similarity[product_index]
        product_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        for i in product_list:
            st.write(f"Brand: {products.iloc[i[0]].Brand}")
            st.write(f"Label: {products.iloc[i[0]].Label}")
            st.write(f"Ingredients: {products.iloc[i[0]].Ingredients}")
            st.write('-' * 50)

# SQLite database search functionality
def sqlite_search_interface():
    st.title("SQLite Database Search")

    ingredient = st.text_input("Enter the ingredient to search for:")

    if st.button("Search"):
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute("SELECT NAME, BRAND FROM COSMETIC_PRODUCT WHERE Ingredients LIKE ?", ('%' + ingredient + '%',))
        rows = c.fetchall()
        conn.close()

        if rows:
            st.write("Results found:")
            for row in rows:
                st.write(row)
        else:
            st.write("No results found.")

# Gemini model response functionality
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
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

def gemino_response_interface():
    st.title("Gemini Model Response")

    input_prompt = """
    As an expert nutritionist, 
    your task is to analyze a food image and provide the following information in the specified format:
    \n1. Calculate the total calories of the food items.
    \n2. Provide details of each food item with their respective calorie intake.
    \nExample format: 
    Item 1 - 100 calories
    Item 2 - 150 calories\n...\n
    Additionally, you are also an expert in recognizing ingredients used in packaged food items. For each ingredient, you need to list its effect on human health and potential side effects and the common terms of each ingredient in the format mentioned above.
    \nPlease provide the required information based on the given food image.
    and also give an score out of 5 based on the ingredients and their overall effect on health
    """
    
    input_gemino = st.text_input("Wish to know something else? ", key="input_gemino")
    uploaded_file_gemino = st.file_uploader("Choose an image for Gemino...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file_gemino is not None:
        image_gemino = Image.open(uploaded_file_gemino)
        st.image(image_gemino, caption="Uploaded Image for Gemino.", use_column_width=True)
    
    submit_gemino = st.button("Submit to get calorie information and ingredient description")

    if submit_gemino:
        image_data = input_image_setup(uploaded_file_gemino)
        response = get_gemini_repsonse(input_gemino, image_data, input_prompt)
        st.subheader("The Response is")
        st.write(response)


# Main function to call individual interfaces based on user choice
def main():
    st.sidebar.title("Choose Functionality")
    option = st.sidebar.selectbox('Select:', ['OCR', 'Product Recommendation', 'SQLite Search', 'Gemino Response'])

    if option == 'OCR':
        ocr_interface()
    elif option == 'Product Recommendation':
        product_recommendation_interface()
    elif option == 'SQLite Search':
        sqlite_search_interface()
    elif option == 'Gemini Response':
        gemino_response_interface()

if __name__ == "__main__":
    main()





#FLASK CODE


# from flask import Flask, render_template, request, redirect, url_for
# from PIL import Image
# import pytesseract  
# import sqlite3
# import streamlit as st
# import pickle
# import pandas as pd 
# from dotenv import load_dotenv
# load_dotenv() 
# import streamlit as st
# import os
# import google.generativeai as genai

# app = Flask(__name__, static_url_path='/static')

# # Load recommendation data
# product_dict = pickle.load(open("product_dict.pkl", "rb"))
# products = pd.DataFrame(product_dict)
# similarity = pickle.load(open("similarity.pkl", "rb"))

# def recommend(product):
#     product_index = products[products['Brand'] == product].index[0]
#     distances = similarity[product_index]
#     product_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
#     recommended_product = []

#     for i in product_list:
#         recommended_product.append(f"Brand: {products.iloc[i[0]].Brand}")
#         recommended_product.append(f"Label: {products.iloc[i[0]].Label}")
#         recommended_product.append(f"Ingredients: {products.iloc[i[0]].Ingredients}")
#         recommended_product.append('-' * 50)  
    
#     return recommended_product

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/', methods=['POST'])
# def upload_image():
#     if 'file' not in request.files:
#         return redirect(request.url)

#     file = request.files['file']

#     if file.filename == '':
#         return redirect(request.url)

#     if file:
#         image_path = 'static/uploads/' + file.filename
#         file.save(image_path)
#         extracted_text = perform_ocr(image_path)  
#         return render_template('index.html', extracted_text=extracted_text, image_path=image_path)

# def perform_ocr(image_path):
#     image = Image.open(image_path)
#     extracted_text = pytesseract.image_to_string(image)
#     return extracted_text

# @app.route('/recommend', methods=['GET', 'POST'])
# def recommend_products():
#     with st.report_thread.add_report_ctx('recommend_products'):
#         st.title("RECOMMENDING PRODUCTS OF SIMILAR BRANDS")

#         unique_brands = products['Brand'].unique()
#         selected_brand_name = st.selectbox('Select brand to check out products', unique_brands)

#         if st.button('RECOMMEND'):
#             recommendation = recommend(selected_brand_name)
#             for i in recommendation:
#                 st.write(i)

#     return st.markdown(st._repr_html_(), unsafe_allow_html=True)

# @app.route('/database_search', methods=['POST'])
# def database_search():
#     ingredient = request.form['ingredient']
#     conn = sqlite3.connect("product.db")
#     cur = conn.cursor()
#     fetch = cur.execute("SELECT NAME, BRAND FROM cosmetic_product WHERE Ingredients LIKE ?", ('%' + ingredient + '%',))
#     rows = fetch.fetchall()
#     cur.close()
#     return render_template('index.html', results=rows)

# if __name__ == '__main__':
#     app.run(debug=True)
