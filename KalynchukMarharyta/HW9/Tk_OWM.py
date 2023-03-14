from pyowm import OWM
import tkinter as tk
from tkinter import font


HEIGHT = 350
WIDTH = 450

def weather_response():
    try:
        owm = OWM('9012e9aca2011c345895e96fb5386be2')
        mgr = owm.weather_manager()
        user_city = entry_field.get()
        observation = mgr.weather_at_place(user_city)
        w = observation.weather
        message = (f"""
        Weather in {user_city}: \n\
        General conditions: {w.detailed_status} \n\
        Wind speed {w.wind()['speed']} mps \n\
        Wind direction {w.wind()['deg']} deg \n\
        Humidity {w.humidity}% \n\
        Max temperature: {w.temperature('celsius')['temp_max']},\n\
        Temperature: {w.temperature('celsius')['temp']}, \n\
        Min temperature: {w.temperature('celsius')['temp_min']} \n\
        Rain: {w.rain} \n\
        Clouds: {w.clouds}
        """)
        return message  
    except: 
        return ('Wrong city name. Please try again')

def get_weather():
    label['text'] = weather_response()



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
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command= lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 8))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

