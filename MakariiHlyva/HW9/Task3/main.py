#------------Weather in your city program----------------

from pyowm import OWM
import tkinter as tk
# from tkinter import font

MY_API_KEY = 'ef2206ff5da67de63306d0b143e20872'
HEIGHT = 350
WIDTH = 450

#-----------Function, which check the weather in entered city----------


def weather_response_from_owm():

  # ---------- FREE API KEY examples ---------------------

  try:
    owm = OWM(MY_API_KEY)
    mgr = owm.weather_manager()

    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather

    result = 'Conditions: ' + w.detailed_status + '\nTemperature ' + str(
      w.temperature("celsius")["temp"]) + '\nWind speed ' + str(
        w.wind()['speed']) + ' km/h' + '\nHumidity of the air is ' + str(
          w.humidity)

    return result

  except:
    result = "You wrote not correct \ncity, ha-ha :) \ntry again"
    return result


def get_weather_in_city():

  label['text'] = weather_response_from_owm()


#-----------------------Graphical Interface-----------------------

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray",
                   fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather_in_city())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5,
                  rely=0.25,
                  relwidth=0.75,
                  relheight=0.6,
                  anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
