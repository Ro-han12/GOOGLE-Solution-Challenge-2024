import streamlit as st 
import pickle
import pandas as pd 

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

        

product_dict=pickle.load(open("product_dict.pkl","rb"))
products=pd.DataFrame(product_dict)

similarity=pickle.load(open("similarity.pkl","rb"))


st.title("RECOMMENDING PRODUCTS OF SIMILAR BRANDS")

unique_brands = products['Brand'].unique()

# Creating  a select box with unique brand values
selected_brand_name = st.selectbox('Select brand to check out products', unique_brands)

if st.button(('RECOMMEND')):
    recommendation=recommend(selected_brand_name)
    for i in recommendation:
        st.write(i)

