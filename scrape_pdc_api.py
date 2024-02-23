import pandas as pd
from sodapy import Socrata
import requests as rq
import datetime
from bs4 import BeautifulSoup as soup 
import psycopg2



# Takes a raw scrape of a list of bills/issues as a string and returns a clean list of bills separated by a comma and a space
def clean_bills_list(bills_raw):
	print(bills_raw)
	bills_upper = str(bills_raw).upper()
	remove_hb_sb_spaces = bills_upper.replace("HB ", "HB").replace("SB ", "SB")
	delimit_with_spaces = remove_hb_sb_spaces.replace(",", " ").replace("/", " ").replace(":", " ").replace(";", " ").replace("-", " ").replace(", ", " ").replace(")", "").replace("(", "")
	bills_list = delimit_with_spaces.split(" ")
	filter_nonnumbers = filter(filter_numbers, bills_list)
	filter_nonhb_sb = filter(filter_hb_sb, filter_nonnumbers)
	return list(filter_nonhb_sb)

def filter_numbers(x):
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	for c in x:
		if c in numbers:
			return True
	return False

def filter_hb_sb(x):
	if "HB" in x:
		return True
	elif "SB" in x:
		return True
	return	False

# Takes an existing dataset and determines if the new row exists in it already
def exists_in_dataset(new, existing):
	return new['id'] in existing['id'].values

# TODO: Add new item to dataset
def add_to_dataset(new):
	#print(f'ADDING {new} to dataset')
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

cursor.execute("SELECT * from pdc ORDER BY receipt_date DESC limit 2000;")
colnames = [desc[0] for desc in cursor.description]

# Fetch all rows from database
record = cursor.fetchall()

record_df = pd.DataFrame.from_records(record)
record_df.columns = colnames

for index, row in results_df.iterrows():
	if exists_in_dataset(row, record_df):
		add_to_dataset(row)