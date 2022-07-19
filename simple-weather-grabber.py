import requests
from bs4 import BeautifulSoup

page = requests.get("https://darksky.net/forecast/29.0721,-82.193/us12/en")
soup = BeautifulSoup(page.content, 'html.parser')
weather_status = soup.find(class_="summary swap").get_text()
feels_like = soup.find(class_="feels-like-text").get_text()
humidity = soup.find(class_="num swip humidity__value").get_text()
uv_index = soup.find(class_="num uv__index__value").get_text()

print(f"General Forecast: {weather_status}")
print(f"Feels Like: {feels_like}")    
print(f"Humidity {humidity}%")
print(f"UV Index: {uv_index}")