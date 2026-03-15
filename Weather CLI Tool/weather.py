import requests, json, os

def get_coords(city_name, API_KEY): # fetches the coordinates of the city for weather url
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    complete_url = base_url + "?q=" + city_name + "&limit=" + "1" + "&appid=" + API_KEY
    response = requests.get(complete_url)
    x = response.json()
    lat = str(x[0]["lat"])
    lon = str(x[0]["lon"])
    return lat, lon

def getWeatherData(city_name): # fetches the weather data of the given city
    
    API_KEY = "" # put your api key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    lat, lon = get_coords(city_name, API_KEY)
    complete_url = base_url + f"?lat={lat}&lon={lon}" + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(complete_url)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "weatherdata.json")
    with open(file_path,"w") as f:
        f.write(response.text)
    return response.json()

def displayWeatherData(response): # takes json response and prints the data in CLI
    print(f"Weather for {response["name"]}")
    print("-------------------------------")
    print(f'''Temperature: {response["main"]["temp"]}
Feels like: {response["main"]["feels_like"]}
Humidity: {response["main"]["humidity"]}
Condition: {response["weather"][0]["description"]}''')
    

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    data = getWeatherData(city_name)
    displayWeatherData(data)

