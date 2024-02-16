import sqlite3
from flask import Flask, render_template ,app,jsonify
connection = sqlite3.connect("product.db")
cursor = connection.cursor()
#table_info = """ CREATE TABLE COSMETIC_PRODUCT(Label varchar(250),Brand varchar(255),Name varchar(255),Price int,Rank int, Ingredients varchar(255),Combination int,Dry int,Normal int,Oily int,Sensitive int)"""
#cursor.execute(table_info)
#cursor.execute(""" drop table COSMETIC_PRODUCT """)

#/Users/rohithr/.vscode/extensions/yy0931.vscode-sqlite3-editor-1.0.171/bin/sqlite3-editor-darwin-arm64 import --database-filepath '/Users/rohithr/Desktop/GOOGLE-Solution-Challenge-2024/product.db' --format csv --table-name 'COSMETIC_PRODUCT' --input-file /Users/rohithr/Desktop/GOOGLE-Solution-Challenge-2024/datasets/cosmetics.csv

import sqlite3

def search_by_ingredient(ingredient):
    # Connect to the SQLite database
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute("SELECT NAME,BRAND FROM COSMETIC_PRODUCT WHERE Ingredients LIKE ?", ('%' + ingredient + '%',))
    rows = c.fetchall()
    conn.close()

    return list(rows)

if __name__ == "__main__":
    ingredient = input("Enter the ingredient to search for: ")
    results = search_by_ingredient(ingredient)

    if results:
        print("Results found:")
        for row in results:
            print(row)
    else:
        print("No results found.")
