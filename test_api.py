import requests
from dotenv import load_dotenv
import os

load_dotenv()

ow_key=os.getenv("ow_key")

def get_country(c_name):
    parameter={
        "q": c_name
    }
    response = requests.get("https://countries.dev/countries", params=parameter, timeout=10)
    return response.json()

def get_all_countries():
    all_objects=[]
    response = requests.get("https://countries.dev/countries", timeout=10)
    data=response.json()
    for country in data:
        all_objects.append(country)
    return all_objects

def get_weather(city):
    parameter={
        "q":city,
        "appid":ow_key,
        "units":"metric"
    }
    header={
        "Authorization":"Bearer"+ ow_key
    }
    try:
        response=requests.get("https://api.openweathermap.org/data/2.5/weather",params=parameter,timeout=10)
        response.raise_for_status()

        data=response.json()
        return data
    except requests.exceptions.HTTPError:
        print("HTTP Error Occurred")

    except requests.exceptions.Timeout:
        print("Request Time Out")

    except requests.exceptions.RequestException:
        print("Error")

def get_forecast(city):
    parameter={
        "q":city,
        "appid":ow_key,
        "units":"metric"
    }
    header={
        "Authorization":"Bearer"+ ow_key
    }
    try:
        response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameter,timeout=10)
        response.raise_for_status()

        data=response.json()
        
        return data
    except requests.exceptions.HTTPError:
        print("HTTP Error Occurred")

    except requests.exceptions.Timeout:
        print("Request Time Out")

    except requests.exceptions.RequestException:
        print("Error")

data = get_forecast("Delhi")
# print(data.keys())
# print((data["list"]))
# print(data["list"][1])
# print(data["list"][2])
# print(data["list"][3])
# print(data["list"][4])