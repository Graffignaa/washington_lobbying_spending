import pandas as pd

unique_bills = pd.read_csv('unique_bills.csv')
bills_raw = unique_bills['bill_number'].tolist()
#print(bills_raw)
bills_1516 = pd.read_csv('./bills/bills_2015-16.csv')
bills_1718 = pd.read_csv('./bills/bills_2017-18.csv')
bills_1920 = pd.read_csv('./bills/bills_2019-20.csv')
bills_2122 = pd.read_csv('./bills/bills_2021-22.csv')
bills_2324 = pd.read_csv('./bills/bills_2023-24.csv')
unique_bills = []
for index, row in bills_1516.iterrows():
	bill = row['bill_number']
	status = row['status_desc']
	if bill in bills_raw:
		unique_bills.append((bill, '1516', status))
for index, row in bills_1718.iterrows():
	bill = row['bill_number']
	status = row['status_desc']
	if bill in bills_raw:
		unique_bills.append((bill, '1718', status))
for index, row in bills_1920.iterrows():
	bill = row['bill_number']
	status = row['status_desc']
	if bill in bills_raw:
		unique_bills.append((bill, '1920', status))		
for index, row in bills_2122.iterrows():
	bill = row['bill_number']
	status = row['status_desc']
	if bill in bills_raw:
		unique_bills.append((bill, '2122', status))
for index, row in bills_2324.iterrows():
	bill = row['bill_number']
	status = row['status_desc']
	if bill in bills_raw:
		unique_bills.append((bill, '2324', status))
	

pd.DataFrame(unique_bills).to_csv('bills_with_status.csv', index=False)	