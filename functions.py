import configs as con
import requests
from datetime import datetime

# only used by CLI
# returns python object that includes all available cities
# object is used in search_cities() function
    # example entry----
    # {
    #     "id": 2960,
    #     "name": "name of city here",
    #     "state": "name of state if applicable",
    #     "country": "two letter country code eg NL",
    #     "coord": {
    #         "lon": 36.321911,
    #         "lat": 34.940079
    #     }
    # }
def city_list():

    import json
    with open("citylist.json", "r", encoding="utf8")as f:
        cities = json.load(f)
    return cities


# used by CLI to search for city by country code and city name.
# requires object from city_list() function as parameter
# returns city and country code variables
# will return nothing if nothing is found
def search_cities(cities):
    search_results =[]
    country = input("Enter 2 letter country code: ").upper()
    print("You can enter the full city name or only part of it")
    print("For example 'amster' or 'amsterdam'")
    yourcity = input("Enter city name: ").capitalize()

    for element in cities:
        if element["country"] != country:
            continue
        elif yourcity not in element["name"]:
            continue
        else:
            search_results.append(element["name"])
    if len(search_results) == 0:
        print("sorry, not found")
        return
    else:
        for index, item in enumerate(search_results):
            print(index,item)
        num = int(input("select a city using the corresponding numbers: "))
        return search_results[num], country


# used by both cli and gui
# formats the api response to a string
# takes a request.json weather report and returns a string of formatted data with descriptions
def format_data_to_string(data):
    description = data["weather"][0]["description"]
    temp = str(data["main"]["temp"])
    Tmax = str(data["main"]["temp_max"])
    Tmin = str(data["main"]["temp_min"])
    humidity = str(data["main"]["humidity"])
    pressure = str(data["main"]["pressure"])
    windspeed = str(data["wind"]["speed"])
    direction = str(data["wind"]["deg"])
    location = data["name"]
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]
    sunrise = datetime.fromtimestamp(sunrise).time()
    sunset = datetime.fromtimestamp(sunset).time()
    var = f"The current weather in {location} is: {description}\nThe temperature is: {temp}C with a min of {Tmin}C and a max of {Tmax}C\n"
    var2 = f"Humidity is {humidity}% and barometric pressure is {pressure} hPa\n"
    var3 = f"The windspeed is {windspeed} m/sec and the wind direction is {direction} degrees \n"
    var4 = f"Sunrise is at {sunrise} and sunset is at {sunset}"
    output = var+var2+var3+var4
    return output


#only used by cli
#Takes a city name and country code and returns a list with weather data
# will quit if API call fails
def api_call(city, country):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={con.api_key}&q={city},{country}&units={con.units}"
    print(city, "api call made")
    request = requests.get(url)
    if request.status_code != 200:
        print(request.status_code)
        print("error with api call")
        quit()
    data = request.json()

    return data


# only used by gui
# takes weather report data from api call and downloads appropriate icon to icon.png file
def download_icon(data):
    icon_code = data["weather"][0]["icon"]
    url = f"http://openweathermap.org/img/wn/{icon_code}@4x.png"
    request = requests.get(url)
    if request.status_code != 200:
        print(request.status_code)
        print("error with api call for image download")
        quit()
    icon_file = open("icon.png", "wb")
    icon_file.write(request.content)
    icon_file.close()


#only used by GUI
#Takes a city name and returns object with weather data
def gui_api_call(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={con.api_key}&q={city}&units={con.units}"
    print(city, "api call made")
    request = requests.get(url)
    if request.status_code != 200:
        print(request.status_code)
        quit()
    data = request.json()
    return data

