import urllib.request
import csv
from bs4 import BeautifulSoup
from datetime import datetime

"""
Web scraper to keep track of the prices of select products from YesStyle.

referred to:

https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2
"""

chunky_pump_oxford = "https://www.yesstyle.com/en/pangmama-chunky-heel-oxfords-black-39/info.html/pid.1036382207"
perforated_oxford = "https://www.yesstyle.com/en/colorful-shoes-perforated-oxford-pumps-black-39/info.html/pid.1035160556"
oxford_pump = "https://www.yesstyle.com/en/pangmama-oxford-pumps/info.html/pid.1048329106"

quote_page = [chunky_pump_oxford, perforated_oxford, oxford_pump]

data = []

for pg in quote_page:
    
    # query website, return html
    page = urllib.request.urlopen(pg)
    # parse html using beautiful soap, store in variable
    soup = BeautifulSoup(page, 'html.parser')
    # Take out <div> and get value
    brand = soup.find('span', attrs={'ng-bind-html': 'productData.product.brandName'}).text.strip()
    product = soup.find('span', attrs={'ng-bind-html': 'productData.product.name'}).text.strip()
    full_name = brand + " - " + product
    
    selling_price = soup.find('div', attrs={'class': 'sellingPrice'}).text.strip()
    list_price = soup.find('span', attrs={'class': 'listPrice'}).text.strip()
    
    print (full_name, selling_price, list_price)
    
    # save data in tuple
    data.append((full_name, selling_price, list_price, datetime.now()))

# open a csv file with append
with open('yesstyle_shoes.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for entry in data:
        writer.writerow([entry[0],None, None, None, None, entry[1], entry[2], entry[3]])
