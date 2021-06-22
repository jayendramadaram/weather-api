import requests
from datetime import datetime

api_key = '050b23126abc246654c48401cb0cb58a'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
r = api_data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")



f = open('weather.txt','w')


f.write("Weather Stats for - {}  || {} \n".format(location.upper(), date_time))
f.write("Current temperature is: {:.2f} deg C \n".format(temp_city))
f.write("Current weather desc  : {} \n".format(weather_desc))
f.write("Current Humidity      :{} \n".format(hmdt))
f.write("Current wind speed    : {} \n".format(wind_spd ))
f.close()

pr_f =  open('weather.txt')
a = pr_f.readlines()
for i in a:
  print(i.strip())

