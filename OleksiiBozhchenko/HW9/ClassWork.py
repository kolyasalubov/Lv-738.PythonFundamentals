from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

city = input("Please enter your city : ")
observation = mgr.weather_at_place(city)
w = observation.weather

# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds                  # 75

print(f"""
The weather in {city} today is:
Temperature : {w.temperature('celsius')['temp']} 'C
Humidity : {w.humidity} %
Clouds : {w.clouds} %
""")