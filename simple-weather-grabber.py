import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.YtcbXnbMKUk")
soup = BeautifulSoup(page.content, 'html.parser')

current_temp = soup.find(class_="myforecast-current-lrg").get_text()
print(current_temp)