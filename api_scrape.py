import pandas as pd
from sodapy import Socrata
from scrape_lib import *
import psycopg2



client = Socrata("data.wa.gov", None)

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


for row in results:
	if not exists_in_dataset(row, record_df):
		add_to_dataset(row)