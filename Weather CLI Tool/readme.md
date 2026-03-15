# Weather CLI Tool

This command-line application fetches real-time weather data for a city entered using the OpenWeather API.
The program retrieves geographic coordinates for the city and then requests current weather information.
Sample data is provided in weatherdata.json

## Features

* Get current weather for any city
* Uses OpenWeather Geocoding API to convert city name to coordinates
* Retrieves temperature, humidity, and weather conditions
* Saves the full API response to a JSON file
* Simple command-line interface
* Error handling not implemented yet.
## Setup

Create an API key from OpenWeather.

Set the API key equal to API_KEY variable inside the script.

## Requirements

Requires an API key from openweathermap. 

## Example Output
Weather for Karachi
-------------------------------
Temperature: 25.09
Feels like: 25.14
Humidity: 57
Condition: haze
