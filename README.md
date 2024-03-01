
<div align="center">
  
  <h1>Washington State Lobbying Spending</h2> 
  <img src=https://cdn.britannica.com/98/4998-050-180D0667/state-flag-field-Daughters-of-the-American-1915.jpg></img>
  
  Every year, over 3 billion dollars are spent in the United States to lobby the government in an effort to influence legislation. This project utilizes publicly available datasets from the Washington State Public Disclosures Commission and LegiScan to analyze trends in this spending over the past 10 years in Washington State.
  
  The Washington State Public Disclosures Commission (PDC) publishes a dataset containing expense reports from lobbying activity in the state via data.wa.gov.  It is available as both bulk CSV downloads and via an API endpoint at https://data.wa.gov/Politics/Lobbyist-compensation-and-expenses-by-funding-sour/857w-6s2r/about_data.  
  
  Each row of data contains information from a single PDC lobbying expense report, including the funding source, the amount of funding provided, the contractor who was hired to lobby a governmental body, and a breakdown of what the funding was used on (Political Contributions, Ads, Personal Expenses, etc.).  Additionally, a link out to the original filing on the PDC website is included, where more information can be found.  Utilizing a web scraper written in python, additional information such as the bill or issue being lobbied for and the body being lobbied were extracted from these reports and added to the dataset.  
  
  The bill numbers were then cleaned and cross referenced with legislation data from LegiScan (https://legiscan.com/WA/datasets) in order to determine the status of each bill.  This allows for analysis of the impact of lobbying spend and activity on the passage of legislation, and can determine the "efficiency" of an organization's lobbying efforts.  
  
</div>
