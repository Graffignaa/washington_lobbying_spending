import pandas as pd

bills_raw = pd.read_csv('bills_list.csv')
unique_bills = []
for index, row in bills_raw.iterrows():
	bills = row['bills_lists'].split(", ")
	for b in bills:
		if not b in unique_bills:
			unique_bills.append(b)

pd.DataFrame(unique_bills).to_csv('unique_bills.csv', index=False)	