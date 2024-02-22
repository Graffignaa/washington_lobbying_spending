import pandas as pd
from sodapy import Socrata
import requests as rq
import datetime
from bs4 import BeautifulSoup as soup 
import psycopg2



# Takes an existing dataset and determines if the new row exists in it already
def exists_in_dataset(new, existing):
	return new['id'] in existing['id'].values

# TODO: Add new item to dataset
def add_to_dataset(new):
	return 1

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.wa.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.wa.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# Most recent 2000 results by receipt date, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("9nnw-c693", limit=2000, order="receipt_date DESC")



# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

connection = psycopg2.connect(database="pdc_data", user="postgres", password="password", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * from pdc limit 100;")

# Fetch all rows from database
record = cursor.fetchall()

record_df = pd.DataFrame.from_records(record)

print("Data from Database:- ", record_df.head)

for index, row in results_df.iterrows():
	if exists_in_dataset(row, record_df):
		add_to_dataset(row)