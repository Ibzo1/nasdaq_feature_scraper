import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
import json


def setup_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    return driver

def parse_institutional_holdings(driver):
    institutional_holdings = []
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='institutional-holdings__table']"))
        )
    except TimeoutError:
        print("Timeout waiting for table to load.")
        return institutional_holdings

    rows = driver.find_elements(By.XPATH, "//table[@class='institutional-holdings__table']/tbody/tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        holding = {
            'Holder': cols[0].text if len(cols) > 0 else '',
            'Shares': cols[1].text if len(cols) > 1 else '',
            'Date Reported': cols[2].text if len(cols) > 2 else '',
            'Percent Outstanding': cols[3].text if len(cols) > 3 else '',
            'Value': cols[4].text if len(cols) > 4 else ''
        }
        institutional_holdings.append(holding)
    return institutional_holdings

def determine_action(percent_change):
    return "bought" if percent_change >= 0 else "sold"

def max_min(ticker):
    url = "https://www.nasdaq.com/market-activity/stocks/{}/institutional-holdings".format(ticker)
    driver = setup_driver()
    driver.get(url)

    try:
        institutional_holdings = parse_institutional_holdings(driver)

        # Convert the list of dictionaries to JSON 
        holdings_json = json.dumps(institutional_holdings, indent=4)
        #print(holdings_json)

        # Extract holder, percent change, shares, and date 
        sorted_data = sorted(
            [
                (d['Holder'], convert_percent_to_float(d['Value']), d['Date Reported'], d['Shares'])
                for d in institutional_holdings
                if d['Value'] and d['Value'].endswith('%')
            ],
            key=lambda x: x[1]
        )

        # Get the highest and lowest percent change
        highest = sorted_data[-1] if sorted_data else None
        lowest = sorted_data[0] if sorted_data else None

        # Format the output
        if highest:
            action = determine_action(highest[1])
            print(f"{highest[0]} {action} {highest[2]} shares on {highest[3]} with {highest[1]}% change")
        if lowest:
            action = determine_action(lowest[1])
            print(f"{lowest[0]} {action} {lowest[2]} shares on {lowest[3]} with {lowest[1]}% change")
  
    finally:
        driver.quit()

def convert_percent_to_float(percent_str):
    try:
        return float(percent_str.strip('%'))
    except ValueError:
        return 0



if __name__ == "__max_min__":
    max_min()


def scrape_institutional_investors(ticker):
    driver = setup_driver()
    driver.get(f"https://www.nasdaq.com/market-activity/stocks/{ticker}/institutional-holdings")
    data = parse_institutional_holdings(driver)
    driver.quit()
    return data
