# from flask import Flask, jsonify
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# app = Flask(__name__)

# @app.route('/scrape-nifty-fifty', methods=['GET'])
# def scrape_nifty_fifty():
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)

#     nifty_fifty_data = {}

#     try:
#         url = 'https://www.nseindia.com/'
#         driver.get(url)
#         time.sleep(10)

#         nifty_fifty_divs = driver.find_elements(By.XPATH, '//div[contains(@class, "form-inline niftyFifty slick-slide") and @aria-hidden="false"]')
#         for div in nifty_fifty_divs:
#             logo_with_text = div.find_element(By.CLASS_NAME, 'logo_with_text').text
#             nifty_fifty_data['logo_with_text'] = logo_with_text

#     finally:
#         driver.quit()

#     return jsonify(nifty_fifty_data)

# @app.route('/scrape-graph-head', methods=['GET'])
# def scrape_graph_head():
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service)

#     graph_head_data = {}

#     try:
#         url = 'https://www.nseindia.com/'
#         driver.get(url)
#         time.sleep(5)

#         graph_head_div = driver.find_element(By.CLASS_NAME, 'graph_head')
#         graph_head_data['tb_index_val'] = graph_head_div.find_element(By.CLASS_NAME, 'tbVal.tbIndexVal').text
#         graph_head_data['open_val'] = graph_head_div.find_element(By.CLASS_NAME, 'openVal').text
#         graph_head_data['high_val'] = graph_head_div.find_element(By.CLASS_NAME, 'highVal').text
#         graph_head_data['low_val'] = graph_head_div.find_element(By.CLASS_NAME, 'lowVal').text

#     finally:
#         driver.quit()

#     return jsonify(graph_head_data)

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

from flask import Flask, jsonify
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/scrape-nifty-fifty', methods=['GET'])
def scrape_nifty_fifty():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    nifty_fifty_data = {}

    try:
        url = 'https://www.nseindia.com/'
        driver.get(url)
        time.sleep(10)

        nifty_fifty_divs = driver.find_elements(By.XPATH, '//div[contains(@class, "form-inline niftyFifty slick-slide") and @aria-hidden="false"]')
        for div in nifty_fifty_divs:
            logo_with_text = div.find_element(By.CLASS_NAME, 'logo_with_text').text
            nifty_fifty_data['logo_with_text'] = logo_with_text

    finally:
        driver.quit()

    return jsonify(nifty_fifty_data)

@app.route('/scrape-graph-head', methods=['GET'])
def scrape_graph_head():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    graph_head_data = {}

    try:
        url = 'https://www.nseindia.com/'
        driver.get(url)
        time.sleep(5)

        graph_head_div = driver.find_element(By.CLASS_NAME, 'graph_head')
        graph_head_data['tb_index_val'] = graph_head_div.find_element(By.CLASS_NAME, 'tbVal.tbIndexVal').text
        graph_head_data['open_val'] = graph_head_div.find_element(By.CLASS_NAME, 'openVal').text
        graph_head_data['high_val'] = graph_head_div.find_element(By.CLASS_NAME, 'highVal').text
        graph_head_data['low_val'] = graph_head_div.find_element(By.CLASS_NAME, 'lowVal').text

    finally:
        driver.quit()

    return jsonify(graph_head_data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
