import requests

# 1. Ask the user for the city
city_name = input("Which city's weather do you want? ")
print(f"🔍 Checking the skies over {city_name}...")

try:
    # 2. Get the coordinates (Geocoding)
    geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    geo_response = requests.get(geocode_url)
    geo_data = geo_response.json()
    
    # Extract latitude and longitude
    latitude = geo_data['results'][0]['latitude']
    longitude = geo_data['results'][0]['longitude']

    # 3. Get the weather using those coordinates
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    # Extract temperature in Celsius
    temp_c = weather_data['current_weather']['temperature']
    
    # 4. Convert Celsius to Fahrenheit
    temp_f = (temp_c * 9/5) + 32

    # 5. Print the final clean output!
    print(f"\n🌡️ Current Weather for {city_name.capitalize()}:")
    print(f"{temp_c}°C")
    print(f"{round(temp_f, 1)}°F")

except IndexError:
    print("❌ Hmm, I couldn't find that city. Check your spelling!")
except Exception as e:
    print(f"❌ Something went wrong: {e}")
