# Import required libraries
import sqlite3
import pandas as pd
  
# Connect to SQLite database
conn = sqlite3.connect('realstate_tn.db')
  
# Load CSV data into Pandas DataFrame
df = pd.read_csv('/Users/ahmedtrifa/Documents/Dev/web-scraper/data/Realstate_la-marsa_immobilier-a-louer_20220406.csv')
df.columns = ["id", "name", "price"]
# Write the data to a sqlite table
df.to_sql('properties', conn, if_exists='replace', index=False)
  
# # Create a cursor object
# cur = conn.cursor()
# # Fetch and display result
# for row in cur.execute('SELECT * FROM student'):
#     print(row)
# # Close connection to SQLite database
# conn.close()