import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"https://weather.com/en-IN/weather/today/l/{city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    current_temp = soup.find("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
    chances_rain = soup.find("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
    temp = current_temp.text
    temp_rain = chances_rain.text
    return temp, temp_rain

def show_weather():
    city = city_entry.get()
    try:
        temp, rain = get_weather(city)
        result = f"Current Temperature: {temp}\nChances of Rain: {rain}"
        messagebox.showinfo("Weather", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Current Weather App")

city_label = tk.Label(root, text="Enter City:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

weather_button = tk.Button(root, text="Get Weather", command=show_weather)
weather_button.pack()

root.mainloop()