# from flask import Flask, render_template, request, redirect, url_for
# from PIL import Image
# import pytesseract
# app = Flask(__name__, static_url_path='/static')

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

# if __name__ == "__main__":
#     app.run(debug = True)
import streamlit as st
from PIL import Image
import pytesseract

def perform_ocr(image):
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def main():
    st.title("OCR with Streamlit")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button('Perform OCR'):
            extracted_text = perform_ocr(image)
            st.write("Extracted Text:")
            st.write(extracted_text)

if __name__ == "__main__":
    main()
