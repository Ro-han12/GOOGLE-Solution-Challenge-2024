import streamlit as st
import sqlite3

# Function to search for products by ingredient in the SQLite database
def search_by_ingredient(ingredient):
    # Connect to the SQLite database
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute("SELECT NAME, BRAND FROM COSMETIC_PRODUCT WHERE Ingredients LIKE ?", ('%' + ingredient + '%',))
    rows = c.fetchall()
    conn.close()
    return rows

def main():
    st.title("Product Search by Ingredient")

    # Get the ingredient from the user
    ingredient = st.text_input("Enter the ingredient to search for:")

    # Perform the search when the user clicks the button
    if st.button("Search"):
        results = search_by_ingredient(ingredient)

        # Display the results
        if results:
            st.write("Results found:")
            for row in results:
                st.write(row)
        else:
            st.write("No results found.")

if __name__ == "__main__":
    main()
