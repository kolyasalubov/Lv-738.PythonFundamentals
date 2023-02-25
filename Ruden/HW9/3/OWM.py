from pyowm import OWM


def get_wather_owm(city_name):
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(city_name)
    w = observation.weather

    result = 'Conditions: ' + w.detailed_status + '\nTemperature ' + str(
      w.temperature("celsius")["temp"]) + '\nWind speed ' + str(
        w.wind()['speed']) + ' km/h' + '\nHumidity ' + str(
          w.humidity)

    return result









