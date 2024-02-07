import sqlite3
connection = sqlite3.connect("product.db")
cursor = connection.cursor()
#table_info = """ CREATE TABLE COSMETIC_PRODUCT(Label varchar(250),Brand varchar(255),Name varchar(255),Price int,Rank int, Ingredients varchar(255),Combination int,Dry int,Normal int,Oily int,Sensitive int)"""
#cursor.execute(table_info)
#cursor.execute(""" drop table COSMETIC_PRODUCT """)
#/Users/rohithr/.vscode/extensions/yy0931.vscode-sqlite3-editor-1.0.171/bin/sqlite3-editor-darwin-arm64 import --database-filepath '/Users/rohithr/Desktop/GOOGLE-Solution-Challenge-2024/product.db' --format csv --table-name 'COSMETIC_PRODUCT' --input-file /Users/rohithr/Desktop/GOOGLE-Solution-Challenge-2024/datasets/cosmetics.csv
