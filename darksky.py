from selenium import webdriver
import time


def get_new_url(location):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get("https://darksky.net/forecast/29.0721,-82.193/us12/en")

    parent = driver.find_element_by_id("searchForm")
    input_element = parent.find_element_by_tag_name("input")
    search_button = driver.find_element_by_class_name("searchButton")

    input_element.clear()
    input_element.send_keys(location)
    search_button.click()
    time.sleep(1)
    return driver.current_url
    
