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
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import pytesseract
import streamlit as st 
import pickle
import pandas as pd 
import sqlite3 

app = Flask(__name__, static_url_path='/static')

# Flask Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        image_path = 'static/uploads/' + file.filename
        file.save(image_path)
        extracted_text = perform_ocr(image_path)  
        return render_template('index.html', extracted_text=extracted_text, image_path=image_path)

def perform_ocr(image_path):
    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

# Streamlit App
def recommend(product):
    product_index = products[products['Brand'] == product].index[0]
    distances = similarity[product_index]
    product_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_product = []

    for i in product_list:
        recommended_product.append(f"Brand: {products.iloc[i[0]].Brand}")
        recommended_product.append(f"Label: {products.iloc[i[0]].Label}")
        recommended_product.append(f"Ingredients: {products.iloc[i[0]].Ingredients}")
        recommended_product.append('-' * 50)  
    
    return recommended_product

def search_by_ingredient(ingredient):
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute("SELECT NAME,BRAND FROM COSMETIC_PRODUCT WHERE Ingredients LIKE ?", ('%' + ingredient + '%',))
    rows = c.fetchall()
    conn.close()

    return list(rows)

if __name__ == "__main__":
    # Run Flask server
    app.run(host='0.0.0.0', port=5000, debug=True)

    # Execute Streamlit App and SQLite Database Functions
    # Note: These parts should be executed after the Flask server starts running
    # Your Streamlit app and SQLite database functions would typically be executed here
