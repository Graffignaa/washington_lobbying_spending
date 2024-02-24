# Code for scraping additional data from the PDC website for bulk csv downloads
import datetime
import pandas as pd
from scrape_lib import *

expenses = pd.read_csv('expenses_cleaned.csv')
out = []
i = 0
csvs = 1
for index, row in expenses.iterrows():

	out_row = scrape_pdc(row, row['url'][13:-1])
	out.append(out_row)

	i += 1
	if i % 100 == 0:
		print(f'Scraped {i} lines.')
	if i == 100:
		print(f'Scraped {i * csvs} lines.  Printing to csv at {datetime.datetime.now()}')
		pd.DataFrame(out).to_csv(f'scraped{csvs}.csv', index=True)
		csvs += 1
		out = []
		i = 0
pd.DataFrame(out).to_csv(f'testscraped{csvs}.csv', index=True)	