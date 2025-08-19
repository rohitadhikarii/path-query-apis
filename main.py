import requests
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

app = FastAPI()
load_dotenv()
api_key = os.getenv("API_KEY")
#Get Github User(Query param)
@app.get("/get_github_user")
def get_user(username: str):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 404: 
        raise HTTPException(status_code=404, detail=f"User:{username} not found")
    if response.status_code == 403:
        raise HTTPException(status_code=403, detail=f"API limit exceeded. Authenticate or Try Again")
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail="Error fetching GitHub user"
        )
    json_data = response.json() #gets the jsonified response
    json_return = {
        "login": json_data["login"],
        "name": json_data["name"],
        "public_repos": json_data["public_repos"],
        "followers": json_data["followers"],
        "following": json_data["following"],
    } #send the particular json back
    return json_return 


#GET Weather data(Path Param)

@app.get("/get_weather/{city}")
def get_weather(city: str):
    if not api_key:
        raise HTTPException(status_code=500, detail="API key is missing.")
    geo_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}").json()
    if not geo_response: #catching invalid city
        raise HTTPException(status_code=404, detail=f"Invalid City:{city}")
    lat, lon = geo_response[0]["lat"], geo_response[0]["lon"]  # stores the geo coordinates
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}").json()
    
    json_return = {
        "city": weather_response["name"],
        "temperature": round(weather_response["main"]["temp"] - 273.15, 2),
        "weather description": weather_response["weather"][0]["description"]
    }
    return json_return
