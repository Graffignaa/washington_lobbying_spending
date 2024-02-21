import requests as rq
import datetime
import pandas as pd
from bs4 import BeautifulSoup as soup 

# Takes a raw scrape of a list of bills/issues as a string and returns a clean list of bills separated by a comma and a space
def clean_bills_list(bills_raw):
	bills_upper = bills_raw.upper()
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

expenses = pd.read_csv('expenses_test.csv')
for index, row in expenses.iterrows():
		issue_bill_number = row['issue_bill_number']
		cleaned = clean_bills_list(issue_bill_number)
		print(cleaned)		




