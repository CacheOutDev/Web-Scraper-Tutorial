# Web-Scraper-Tutorial

This is a web scraper for files under the same domain names. At the end, the information is compiled into spreadsheet and downloaded to the user's Downloads folder.

The user provides a link address and requests.get() grabs data from the webpage. BeautifulSoup is used to web scrape the HTML.  Throughout the code, Regex and BeautifulSoup are used to filter the HTML and compile relevant information. HREF values and link text are collected and added to lists. These lists are translated into Pandas series, which are then combined into one Pandas dataframe. This dataframe is saved to an Excel workbook and downloaded to the user's Downloads folder.

To use the program, when the terminal generates a prompt, provide a link address to a webpage full of domain-related documents.
