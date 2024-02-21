# Code for scraping additional data from the PDC website for bulk csv downloads

import requests as rq
import datetime
import pandas as pd
from bs4 import BeautifulSoup as soup 

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

expenses = pd.read_csv('expenses_cleaned.csv')
out = []
i = 0
csvs = 1
for index, row in expenses.iterrows():

	url = row['url'][13:-1]

	page_soup = soup(rq.get(url).text, 'html.parser')
	#print(url)
	lobbying_activity = page_soup.find('div',id='l2_lobbying_activity')
	#print(lobbying_activity)
	if(lobbying_activity):
		lobbying_table = lobbying_activity.find('table')
		#print(lobbying_table)
		if(lobbying_table):
			lobbying_df = pd.read_html(lobbying_table.prettify())[0]
			#print(lobbying_df)

			employer = row['employer_name']
			#print(employer)

			legislation_subject_matter = ""
			issue_bill_number = ""
			committee_lobbied = ""
			for lobbying_index, lobbying_row in lobbying_df.iterrows():
				if lobbying_row['Employer'] == employer:
					legislation_subject_matter = lobbying_row['Subject Matter of Proposed Legislation']
					print(lobbying_row['Issue or bill number'])
					issue_bill_number = clean_bills_list(lobbying_row['Issue or bill number'])
					committee_lobbied = lobbying_row['Persons, Legislative committee or State Agency considering the matter']
					break
			# for item in page_soup:
			# 	if item.id == "l2_lobbying_activity":
			# 		print(item)
			out_row = row
			out_row['legislation_subject_matter'] = legislation_subject_matter
			out_row['issue_bill_number'] = issue_bill_number
			out_row['committee_lobbied'] = committee_lobbied
			out.append(out_row)
	i += 1
	if i % 500 == 0:
		print(f'Scraped {i} lines.')
	if i == 100:
		print(f'Scraped {i * csvs} lines.  Printing to csv at {datetime.datetime.now()}')
		pd.DataFrame(out).to_csv(f'scraped{csvs}.csv', index=True)
		csvs += 1
		out = []
		i = 0
pd.DataFrame(out).to_csv(f'scraped{csvs}.csv', index=True)	