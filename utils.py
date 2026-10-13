from storage import save_destination
from test_api import get_weather,get_forecast
def country_info(country):

    print("==============================")
    print("       COUNTRY INFO")
    print("==============================")
    print("Country   :",country["name"])
    print("Capital   :",country.get("capital"))
    print("Currency  :",country["currencies"][0]["name"])
    print("Flag      :",country["flag"])
    print("==============================")
    capital=country.get("capital")
    if capital:
        weather_data=get_weather(capital)
        forecast_data=get_forecast(capital)
        weather_info(weather_data)
        forecast_info(forecast_data)
    else:
        print("Weather Information is Unavailable!!")
    saved=input("Do you want to save this destination? (yes/no)")
    dest_dict={
        "country":country["name"],
        "capital":country.get("capital"),
        "currency":country["currencies"][0]["name"],
        "flag":country["flag"]      
        }
    
    if saved.lower()=="yes":
        result=save_destination(dest_dict)
        if result: 
            print("Destination saved successfully!!")
        else:
            print("Already saved!!")

def weather_info(data):
    print("==============================")
    print("         Weather Info.        ")
    print("------------------------------")
    print("Weather in :",data["name"])
    print("Temperature:",data["main"]["temp"])
    print("Feels like:",data["main"]["feels_like"])
    print("Humidity:",data["main"]["humidity"])
    print("Condition :", data["weather"][0]["main"])
    print("Description:",data["weather"][0]["description"])
    print("Wind speed:",data["wind"]["speed"])
    print("==============================")


def forecast_info(data):
    dates=[]
    print("======================================================")
    print("         5-DAY WEATHER FORECAST")
    print("------------------------------------------------------")
    for record in data["list"]:
        date=record["dt_txt"][:10]
        
        if date not in dates:
            condition=record["weather"][0]["description"]
            if "thunderstorm" in condition:
                icon="⛈️"
            elif "drizzle" in condition or "rain" in condition:
                icon = "🌧️"
            elif "snow" in condition:
                icon = "❄️"
            elif "few clouds" in condition:
                icon = "🌤️"
            elif "scattered clouds" in condition:
                icon = "⛅"
            elif "broken clouds" in condition or "overcast clouds" in condition:
                icon = "☁️"
            elif "cloud" in condition:
                icon = "☁️"
            elif "clear" in condition:
                icon = "☀️"
            elif "mist" in condition or "fog" in condition or "haze" in condition:
                icon = "🌫️"
            else:
                icon = "🌤️"
            print(f"{icon} {date} | {record["main"]["temp"]:.1f}°C | Condition: {condition}")
            dates.append(date)
    print("------------------------------------------------------")
