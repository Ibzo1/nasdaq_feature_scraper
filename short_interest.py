from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json
from selenium.webdriver.common.by import By

def scrape_short_interest(ticker):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    driver.get(f"https://www.nasdaq.com/market-activity/stocks/{ticker}/short-interest")
    time.sleep(5)

    data = []
    for row in driver.find_elements(By.CSS_SELECTOR, '.short-interest__row.short-interest__row--body'):
        date = row.find_element(By.CSS_SELECTOR, 'th').text
        interest = row.find_element(By.CSS_SELECTOR, '.short-interest__cell--interest').text
        avg_daily_volume = row.find_element(By.CSS_SELECTOR, '.short-interest__cell--avgDailyShareVolume').text
        days_to_cover = row.find_element(By.CSS_SELECTOR, '.short-interest__cell--daysToCover').text

        row_data = {
            'Date': date,
            'Short Interest': interest,
            'Average Daily Share Volume': avg_daily_volume,
            'Days To Cover': days_to_cover
        }
        data.append(row_data)

    driver.quit()
    return data
