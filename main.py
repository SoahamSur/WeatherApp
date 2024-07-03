import requests
import pyttsx3
import json

engine = pyttsx3.init()
engine.setProperty('rate', 150)

api_key = "Your_api_Key"

def get_weather_info(location):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

        # Fetch weather data
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        weatherdict = response.json()

        giveInfo = [
            f"Current temperature at {location} is {weatherdict['current']['temp_c']} degree Celsius",
            f"Current weather condition is {weatherdict['current']['condition']['text']}",
            f"Feels like temperature is {weatherdict['current']['feelslike_c']} degree Celsius",
            f"Humidity is {weatherdict['current']['humidity']}%",
            f"Precipitation is {weatherdict['current']['precip_mm']} mm",
            f"Cloud cover is {weatherdict['current']['cloud']}%"
        ]

        for info in giveInfo:
            engine.say(info)
        
    except requests.exceptions.RequestException as e:
        engine.say("Failed to fetch weather data. Please check your internet connection and try again.")
    except KeyError as e:
        engine.say("Unexpected data format received from the weather service.")
    except Exception as e:
        engine.say(f"An error occurred: {str(e)}")
    finally:
        engine.say("Thank You for using our service")
        engine.runAndWait()

engine.say("Enter your location: ")
engine.runAndWait()
location = input("-> ")

get_weather_info(location)

