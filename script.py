import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import certifi
import os

# Lines 9 - 11: User provides a link address. Requests.get() grabs the page data and BeautifulSoup scrapes the HTML
page_link = input("Enter the link address of the webpage that you'd like to scrape.")
page_request = requests.get(page_link, verify=certifi.where())
soup = BeautifulSoup(page_request.content, "html.parser")

link_name, link_address, evaluation_status = [], [], []

# link_patterns establishes the domain name that the files share
# relevant_links collects all the file links that share teh established domain name
link_patterns = re.compile(r'____')
relevant_links = soup.find_all(href=link_patterns)

# Lines 23 - 31
# If the page has relevant links, each link's text and href values are saved to lists
# If there are no relevant links, then the spreadsheet will read "No links present on this page."
if len(relevant_links) != 0:
    for relevant_link in relevant_links:
        link_name.append(relevant_link.get_text())
        link_address.append(relevant_link.get('href'))
        evaluation_status.append(' ')
else:
    link_name.append('No links present on this page.')
    link_address.append(' ')
    evaluation_status.append(' ')

# Lines 31 - 39: the lists are saved as series and compiled as a singular data frame.
df = pd.DataFrame(link_name, columns = ['Link Name'])
df['Link Address'] = link_address
df['Link has been evaluated'] = evaluation_status

excel_html = soup.find(______)
excel_name = excel_html.get_text()

# Lines 42 - 49: the dataframe is saved as an Excel workbook and downloaded to the user's Downloads folder
df = df.to_excel(excel_name + ".xlsx")

file_path = "/Users/username/Downloads"
file = os.path.join(file_path, df)

open(file, "wb").write(page_request.content)

print("Downloaded: " + str(file))
