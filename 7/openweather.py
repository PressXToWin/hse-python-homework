from http.client import HTTPException

import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY не найден")

def main():
    city = input("Введите название города: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if not response.status_code == 200:
        raise HTTPException(response.status_code)

    weather_data = response.json()

    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]

    print(f"Температура: {temp} С")
    print(f"Описание: {description}")

if __name__ == "__main__":
    main()