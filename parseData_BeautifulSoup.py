import bs4 as bs
import urllib3
import csv
import os

# constants go here
URL = 'https://www.mohfw.gov.in/'
FILEPATH = '/home/covid19dashboard/Covid19India/output.csv'

# connect to the website
try:
    os.remove(FILEPATH)
    print("File deleted successfully...")
except:
    print("Error while deleting file ", FILEPATH)

http = urllib3.PoolManager()

source = http.request('GET', url=URL).data
soup = bs.BeautifulSoup(source, 'lxml')

# parse table locating div
parentDiv = soup.find("div", {"class": "content newtab"})
childDiv = parentDiv.find("div", {"class": "table-responsive"})
table = childDiv.find('table')

# populating table data as list
table_rows = table.find_all('tr')
output_rows = []
row_count = 0
headers = ["S. No."
    ,"Name of State / UT"
    ,"Confirmed cases (Indians)"
    ,"Confirmed cases (Foreigners)"
    ,"Cured/Discharged"
    ,"Death"]

# transform table data for CSV file
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text
               .replace('\n', '')
               .replace('Union Territory of ', '')
               .replace('number of confirmed cases in India', 'cases') for i in td]
    print(row)
    if len(row) == 5:
        row.insert(0, str(row_count))
    output_rows.append(row)
    row_count += 1

# write table data to CSV
with open(FILEPATH, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(output_rows)

print("Data received ...")