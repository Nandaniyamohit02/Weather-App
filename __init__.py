# import Lib & Framwork
from datetime import date
import solara
import requests
import os
from dotenv import load_dotenv

def city_data(city,api):
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api}").json()
    if data['cod'] == '404':
        data = "none"
    return data

# City_Country
def city_country(data):
    try:
        Country = data["sys"]["country"]
    except:
        Country = "none"
    return Country

# City_Temp
def city_temp(data):
    try:
        Temp = data["main"]["temp"]
    except:
        Temp = 00.00
    return Temp

# City_Name
def city_name(data):
    try:
        Name = data["name"]
    except:
        Name = text.value
    return Name

# City_Desc
def city_desc(data):
    try:
        Desc = data["weather"][0]["main"]
    except:
        Desc = "none"
    return Desc

# City_Min_Temp
def city_min_temp(data):
    try:
        Temp = data["main"]["temp_min"]
    except:
        Temp = "00:00"
    return Temp

# City_Max_Temp
def city_max_temp(data):
    try:
        Temp = data["main"]["temp_max"]
    except:
        Temp = "00:00"
    return Temp

# Date_Now
def date_now():
    today = date.today()
    try:
        dt = today.strftime("%d/%m/%Y")
    except:
        dt = "00/00/0000"
    return dt

# api key from .env file
api_key = os.getenv("api_key")

text = solara.reactive("junagadh")
continuous_update = solara.reactive(True)

gutters = solara.reactive(True)
gutters_dense = solara.reactive(True)

# main function buitin copy componets
# for Day/Night Theme
@solara.component
def ThemeToggle(
    on_icon: str = "mdi-weather-night",
    off_icon: str = "mdi-weather-sunny",
):
    ...
# for Title
@solara.component
def Title(title: str):
    ...

# main
@solara.component
def Page():

    load_dotenv()
    # call all function and store in variable
    City_Data = city_data(text.value,api_key)
    City_F = city_temp(City_Data)
    City_C = round((city_temp(City_Data)-32)*5/9)
    City_Desc = city_desc(City_Data)
    City_Country = city_country(City_Data)
    City_Name = city_name(City_Data)
    City_Max_Temp = city_max_temp(City_Data)
    City_Min_Temp = city_min_temp(City_Data)
    Date_Now=date_now()

    # for AppBar
    with solara.AppBarTitle():
        solara.lab.ThemeToggle(enable_auto=False)
        solara.Text("Weather")

    # for Display
    with solara.Columns([1, 3], gutters=gutters.value, gutters_dense=gutters_dense.value):
        with solara.Card("Location",margin=6,elevation=9):
            solara.InputText("Enter City Name", value=text, continuous_update=continuous_update.value)
        with solara.Card("Display",margin=2,elevation=0):
            solara.Text("Date : ",style="color: #708090; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
            solara.Text(str(Date_Now),style="color: #708090; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
            with solara.Columns([2,2,4], gutters=gutters.value, gutters_dense=gutters_dense.value):
                with solara.Column(align="center"):
                    with solara.Card(margin=5,elevation=1):
                        solara.Text(str(City_Name),style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
                        solara.Text(str(City_Country),style="color: #50a647; font-size: 15px; font-weight: 200; font-family: Arial, Helvetica, sans-serif;margin-left:9px")
                with solara.Column(align="start"):
                    with solara.Card(margin=5,elevation=1):
                        solara.Text(str(City_C),style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
                        solara.Text("°C",style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
                with solara.Column(align="start"):
                    with solara.Card(margin=5,elevation=1):
                        solara.Text(str(City_F),style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
                        solara.Text("°F",style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
                        solara.Text(str(City_Desc),style="color: #50a647; font-size: 15px; font-weight: 200; font-family: Arial, Helvetica, sans-serif;margin-left:9px")
                with solara.Column(align="end"):
                    with solara.Card(margin=2,elevation=1):
                        solara.Text("Max:",style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
                        solara.Text(str(City_Max_Temp),style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
                        solara.Markdown(" ",style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
                        solara.Text("Min:",style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")
                        solara.Text(str(City_Min_Temp),style="color: #50a647; font-size: 30px; font-weight: 500; font-family: Arial, Helvetica, sans-serif;")

# <----------- End ------------>