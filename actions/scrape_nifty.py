# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Set up WebDriver options
# options = Options()
# options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# # Set up WebDriver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# try:
#     # Navigate to the NSE India website
#     url = 'https://www.nseindia.com/'
#     driver.get(url)
    
#     # Wait for the page to load completely
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "niftyFifty")]')))

#     # Scrape data from the div with class 'form-inline niftyFifty slick-slide' when aria-hidden is 'false'
#     nifty_fifty_data = {}
#     nifty_fifty_divs = driver.find_elements(By.XPATH, '//div[contains(@class, "form-inline niftyFifty slick-slide") and @aria-hidden="false"]')
#     for div in nifty_fifty_divs:
#         logo_with_text = div.find_element(By.CLASS_NAME, 'logo_with_text').text
#         nifty_fifty_data['logo_with_text'] = logo_with_text

#     # Print nifty fifty data
#     print("Nifty Fifty Data:")
#     for key, value in nifty_fifty_data.items():
#         print(f"{key}: {value}")

#     # Scrape data from the div with class 'graph_head'
#     graph_head_div = driver.find_element(By.CLASS_NAME, 'graph_head')
#     tb_index_val = graph_head_div.find_element(By.CLASS_NAME, 'tbVal.tbIndexVal').text
#     open_val = graph_head_div.find_element(By.CLASS_NAME, 'openVal').text
#     high_val = graph_head_div.find_element(By.CLASS_NAME, 'highVal').text
#     low_val = graph_head_div.find_element(By.CLASS_NAME, 'lowVal').text

#     # Print graph head data
#     print("\nGraph Head Data:")
#     print(f"Nifty index: {tb_index_val}")
#     print(f"open value: {open_val}")
#     print(f"high value: {high_val}")
#     print(f"low value: {low_val}")

# finally:
#     driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get('http://127.0.0.1:5501/Rasa/web.html')

# Find the table element
table = driver.find_element(By.TAG_NAME, 'table')

# Get all rows in the table
rows = table.find_elements(By.TAG_NAME, 'tr')

# Print header
header = ['Date', 'Nifty 50 Index', 'Open', 'High', 'Low', 'Close']
print("{:<12} {:<15} {:<10} {:<10} {:<10} {:<10}".format(*header))

# Iterate through the rows and print data
for row in rows[2:]:  # Skip the first two header rows
    cols = row.find_elements(By.TAG_NAME, 'td')
    cols = [col.text for col in cols]
    print("{:<12} {:<15} {:<10} {:<10} {:<10} {:<10}".format(*cols))

# Close the WebDriver
driver.quit()
