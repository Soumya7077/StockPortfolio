import csv

recFields = ['STOCK CODE', 'STOCK NAME']
rows = [['RELIANCE', 'Reliance Industries Limited'],
        ['TCS', 'Tata Consultancy Services Limited'],
        ['HDFCBANK', 'HDFC Bank Limited'],
        ['INFY', 'Infosys Limited'],
        ['ICICIBANK', 'ICICI Bank Limited'],
        ['HINDUNILVR', 'Hindustan Unilever Limited'],
        ['SBIN', 'State Bank of India'],
        ['BAJFINANCE', 'Bajaj Finance Limited'],
        ['HDFC', 'Housing Development Finance Corporation Limited'],
        ['BHARTIARTL', 'Bharti Airtel Limited']
        ]
csvFileName = "Stock Details.csv"
with open(csvFileName, 'w') as fp:
    csvwriter = csv.writer(fp)
    csvwriter.writerow(recFields)
    csvwriter.writerows(rows)
