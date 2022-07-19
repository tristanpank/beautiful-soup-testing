import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from darksky import get_new_url

location = input("Please Enter a location: ")
url = get_new_url(location)

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
weather_status = soup.find(class_="summary swap").get_text()
feels_like = soup.find(class_="feels-like-text").get_text()
humidity = soup.find(class_="num swip humidity__value").get_text()
uv_index = soup.find(class_="num uv__index__value").get_text()

print(f"General Forecast: {weather_status}")
print(f"Feels Like: {feels_like}")    
print(f"Humidity {humidity}%")
print(f"UV Index: {uv_index}")