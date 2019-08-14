#Using OpenWeather App to find Current Temperature
import requests
city=input("City Name:")
url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=1da35741c11797f0de2c86ee06bdf01d".format(city)
data=requests.get(url)
res=data.json()
tempature=res['main']
print(tempature)
