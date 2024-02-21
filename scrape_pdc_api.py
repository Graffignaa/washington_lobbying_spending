import pandas as pd
from sodapy import Socrata
import requests as rq
import datetime
from bs4 import BeautifulSoup as soup 

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
results = client.get("9nnw-c693", limit=2000, order="receipt_date ASC")

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# Load existing dataset - this will change
expenses = pd.read_csv('expenses_cleaned.csv')
