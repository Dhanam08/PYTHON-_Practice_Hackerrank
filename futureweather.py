import requests
import json
city=input("City Name:")
url="https://openweathermap.org/data/2.5/forecast/hourly?q={}&appid=1da35741c11797f0de2c86ee06bdf01d".format(city)
data=requests.get(url)
res=data.json()
tempature=res['list']
print(tempature)
