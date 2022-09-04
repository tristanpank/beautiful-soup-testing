from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def get_new_url(location):
    # op = webdriver.ChromeOptions()
    # op.add_argument('headless')
    driver = webdriver.Chrome("C:/Users/trist/Downloads/chromedriver_win32/chromedriver")
    driver.get("https://darksky.net/forecast/29.0721,-82.193/us12/en")

    parent = driver.find_element(By.ID, "searchForm")
    input_element = parent.find_element(By.TAG_NAME, "input")
    search_button = driver.find_element(By.CLASS_NAME, "searchButton")

    input_element.clear()
    input_element.send_keys(location)
    search_button.click()
    time.sleep(1)
    return driver.current_url
    
