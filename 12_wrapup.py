# ---------------------------------------------------------------------------------------
# Purpose of Program: This is to access Current Weather Data based on City or zip Code.
# It will allow user choice of temperature units (Celsius vs Fahrenheit).
# Course: Python for Everybody
# Programming Assignment: Wrapup Project
# Author: Rajendra Prasad Poloju
# Date: 11/16/2024
# ----------------------------------------------------------------------------------------

"""
    Change#: 1
    Change(s) Made: Weather Forecast Application .
    Date of Change:11/16/2024
    Author: Rajendra Prasad Poloju
    Change Approved by: Rajendra Prasad Poloju
    Date Moved to Production:11/16/2024
"""
import requests


class OpenWeatherMapAPIError(Exception):
    """Custom exception for Open Weather Map API related errors"""
    pass


# API configuration
class OpenWeatherMapConfig:
    # API endpoints and authentication key
    OPEN_WEATHER_MAP_WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
    OPEN_WEATHER_MAP_GEO_URL = "http://api.openweathermap.org/geo/1.0/"
    API_KEY = "58b15bdc942e202c1e6d751bea67c884"
    TIMEOUT = 30


# This Prints a separator line for better display
def print_separator():
    print("=" * 100)


# This Prints a separator line for internal steps
def print_internal_separator():
    print("=" * 50)


config = OpenWeatherMapConfig()


# This is to get the weather based on latitude, longitude by invoking Open Weather Map Weather API
def get_weather_by_coordinates(latitude, longitude, temperature_unit):
    try:
        query_params = {
            "lat": latitude,
            "lon": longitude,
            "appId": config.API_KEY,
            "units": temperature_unit
        }
        api_headers = {'cache-control': "no-cache"}
        apiresponse = requests.request("GET", config.OPEN_WEATHER_MAP_WEATHER_URL, headers=api_headers,
                                       params=query_params,
                                       timeout=config.TIMEOUT)
        apiresponse.raise_for_status()
        return apiresponse.json()
    except requests.exceptions.Timeout:
        raise OpenWeatherMapAPIError("Connection timed out while accessing weather service")
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            raise OpenWeatherMapAPIError("Weather data not found for this location")
        raise OpenWeatherMapAPIError(f"HTTP error occurred: {error}")
    except requests.exceptions.ConnectionError:
        raise OpenWeatherMapAPIError("Could not connect to weather service")
    except (KeyError, ValueError):
        raise OpenWeatherMapAPIError("Received invalid data from weather service")


# This is to display  Weather Information.
def display_weather_info(weather_info, temperature_unit):
    if not weather_info:
        return
    temp_unit = "°C" if temperature_unit == "metric" else "°F"  # Determine temperature unit symbol
    print_internal_separator()
    print("     Weather Information")
    print_internal_separator()
    print(f"    Location: {weather_info['name']}, {weather_info['sys']['country']}")
    print(f"    Current Temperature: {weather_info['main']['temp']:.1f}{temp_unit}")
    print(f"    Feels Like: {weather_info['main']['feels_like']:.1f}{temp_unit}")
    print(f"    Low Temperature: {weather_info['main']['temp_min']:.1f}{temp_unit}")
    print(f"    High Temperature: {weather_info['main']['temp_max']:.1f}{temp_unit}")
    print(f"    Pressure: {weather_info['main']['pressure']} hPa")
    print(f"    Humidity: {weather_info['main']['humidity']}%")
    print(f"    Current Weather: {weather_info['weather'][0]['description'].title()}")
    print_internal_separator()


# this is get the coordinates based on zip code by invoking Open Weather Map's geo API
def get_coordinates_by_zipcode(zip_code):
    try:
        query_params = {
            "zip": f"{zip_code},US",
            "appId": config.API_KEY
        }
        api_headers = {'cache-control': "no-cache"}
        zipcode_api_url = config.OPEN_WEATHER_MAP_GEO_URL + "zip"
        apiresponse = requests.request("GET", zipcode_api_url, headers=api_headers, params=query_params,
                                       timeout=config.TIMEOUT)
        apiresponse.raise_for_status()
        appdata = apiresponse.json()
        if not appdata:
            raise OpenWeatherMapAPIError(f"No location found for Zip code : {zip_code}")
        return appdata['lat'], appdata['lon']
    except requests.exceptions.Timeout:
        raise OpenWeatherMapAPIError("Connection timed out while accessing weather service")
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            raise OpenWeatherMapAPIError("Weather data not found for this location")
        raise OpenWeatherMapAPIError(f"HTTP error occurred: {error}")
    except requests.exceptions.ConnectionError:
        raise OpenWeatherMapAPIError("Could not connect to weather service")
    except (KeyError, ValueError):
        raise OpenWeatherMapAPIError("Received invalid data from weather service")


# this is get the coordinates based on City and State Code by invoking Open Weather Map's geo API
def get_coordinates_by_city(city_name, state_code):
    try:
        query_params = {
            "q": f"{city_name},{state_code},US",
            "limit": 1,
            "appId": config.API_KEY
        }
        api_headers = {'cache-control': "no-cache"}
        zipcode_api_url = config.OPEN_WEATHER_MAP_GEO_URL + "direct"
        apiresponse = requests.request("GET", zipcode_api_url, headers=api_headers, params=query_params,
                                       timeout=config.TIMEOUT)
        apiresponse.raise_for_status()
        appdata = apiresponse.json()
        if not appdata:
            raise OpenWeatherMapAPIError(f"No location found for {city_name}, {state_code}")
        return appdata[0]['lat'], appdata[0]['lon']
    except requests.exceptions.Timeout:
        raise OpenWeatherMapAPIError("Connection timed out while accessing weather service")
    except requests.exceptions.HTTPError as error:
        if error.response.status_code == 404:
            raise OpenWeatherMapAPIError("Weather data not found for this location")
        raise OpenWeatherMapAPIError(f"HTTP error occurred: {error}")
    except requests.exceptions.ConnectionError:
        raise OpenWeatherMapAPIError("Could not connect to weather service")
    except (KeyError, ValueError):
        raise OpenWeatherMapAPIError("Received invalid data from weather service")


def weather_by_zipcode(temperature_unit):
    zip_code = input("Enter ZIP code: ").strip()
    if not zip_code.isdigit() or len(zip_code) != 5:  # Zip Code Validation to see if a valid code is entered
        print("Invalid ZIP code. Please enter a 5-digit ZIP code.")
    else:
        latitude, longitude = get_coordinates_by_zipcode(zip_code)
        weather_info = get_weather_by_coordinates(latitude, longitude, temperature_unit)
        display_weather_info(weather_info, temperature_unit)


def valid_state_code(state_code):
    # List of valid US state codes
    valid_states = {
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    }
    return bool(state_code.upper() in valid_states)


def weather_by_city(temperature_unit):
    city_name = input("Enter city name: ").strip()
    if not city_name:
        print("City name cannot be empty.")
    else:
        state_code = input("Enter state code (example - TX for Texas): ").strip().upper()

        if not valid_state_code(state_code):
            print("Invalid state code. Please enter a valid two-letter state code.")
        else:
            latitude, longitude = get_coordinates_by_city(city_name, state_code)
            weather_info = get_weather_by_coordinates(latitude, longitude, temperature_unit)
            display_weather_info(weather_info, temperature_unit)


temperature_options = """Enter Temperature Unit
Enter C for Celsius
Enter F for Fahrenheit
Your Temperature Unit Choice:"""


# this is get request user to enter temperature unit choice
def get_temperature_unit():
    temperature_unit = input(temperature_options).strip()
    if temperature_unit == 'C':
        return 'metric'
    elif temperature_unit == 'F':
        return 'imperial'
    else:
        print("InValid Temperature Unit Option. Defaulted to Fahrenheit.")
        return 'imperial'


user_options = """Enter Z to lookup based on Zip Code
Enter C to lookup based on City, State
Enter X to Exit
Your Geo Location Choice:"""


def main():
    print_separator()
    print("Welcome to Weather Forecast Application!")
    while True:
        try:
            print_separator()
            print("New Weather Forecast Lookup!!!!!")
            print_separator()
            user_choice = input(user_options).strip().lower()
            temperature_unit = "metric"
            if user_choice == 'z' or user_choice == 'c':  # Ask user for temperature unit only if valid lookup is entered
                print_internal_separator()
                temperature_unit = get_temperature_unit()
                print_internal_separator()

            if user_choice == 'z':
                weather_by_zipcode(temperature_unit)
            elif user_choice == 'c':
                weather_by_city(temperature_unit)
            elif user_choice == 'x':
                print("Thank you for using the Weather Forecast Application!")
                break
            else:
                print("Invalid Choice - Please Enter Z,C or X.")

            print_internal_separator()
            exit_choice = input("Do you want perform another lookup?\nType Y to Continue or X to Exit:").strip().lower()
            if exit_choice == 'y':
                continue
            elif exit_choice == 'x':
                print("Thank you for using Weather Forecast Application!")
                break
        except OpenWeatherMapAPIError as error:
            print(f"Open Weather Map API Error : {str(error)}")
        except Exception as error:
            print(f"Unexpected error occurred: {str(error)}")
            print("Please try again.")


if __name__ == "__main__":
    main()
