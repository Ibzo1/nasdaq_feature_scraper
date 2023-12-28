import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def scrape_options_chain(ticker):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    driver.get(f"https://www.nasdaq.com/market-activity/stocks/{ticker}/option-chain")
    time.sleep(5)
    wait = WebDriverWait(driver, 10)  # Adjust time as necessary
    table_rows = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//table[@class="option-chain-tables__table"]//tr')))

    data = []
    for row in table_rows:
        cells = row.find_elements(By.XPATH, './/td')
        if len(cells) > 0:  # Ensure the row contains cells
            row_data = {
                'Expiration Date': cells[1].text,
                'Last': cells[2].text,
                'Change': cells[3].text,
                'Bid': cells[4].text,
                'Ask': cells[5].text,
                'Volume': cells[6].text,
                'Open Interest': cells[7].text,
                'Strike': cells[9].text,
                # ... add other fields as necessary
            }
            data.append(row_data)

        # Convert the list of data into JSON
    json_data = json.dumps(data, indent=4)

    driver.quit()
    return data
