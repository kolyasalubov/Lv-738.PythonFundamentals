from pyowm import OWM

owm = OWM('5a22c5fecf045ec6a863c8e176cc9bc4')
mgr = owm.weather_manager()

place = input("City: ")

observation = mgr.weather_at_place(place)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
temp = w.temperature('celsius')

print(f"In {place} it's {temp['temp']} degrees and lowest/highest temperature should be"
      f" {temp['temp_min']}/{temp['temp_max']}.\nHumidity is {w.humidity}\n"
      f"And wind speed is {w.wind()['speed']}")