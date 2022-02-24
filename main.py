import requests
import os
from datetime import datetime

APP_ID = "dc2ea15b"
APP_KEY = "09eb27bf25eccc86a8f888490c0ef15e"
BASIC_TOKEN = "Q2h1dGRhbmFpOmdidnNlcjM1MXZ6eGQzOHI1MQ"

WEIGHT = 73.5
HEIGHT = 175
AGE = 24

ASK_EXERCISE = input("Tell me whice  excercises you did: ")

TODAY = datetime.now()

TIME = TODAY.strftime("%X")
DATE = TODAY.strftime("%d/%m/%Y")

HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

document_exercise = {
    "query": ASK_EXERCISE,
    "gender":"female",
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}

response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=document_exercise, headers=HEADER)
result = response.json()

URL_POST = "https://api.sheety.co/f111df78d6a40236d9e250d3b887fc60/myWorkoutsSpreadsheet/workouts"
exercise = result["exercises"]

header_post = {
    "Authorization": f"Basic {BASIC_TOKEN}",
	"Content-Type": "application/json"
}

for ex in exercise:
    document_to_post = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": ex["name"].title(),
            "duration": ex["duration_min"],
            "calories": ex["nf_calories"]
        }
    }

    response_post_to_sheet = requests.post(url=URL_POST, json=document_to_post, headers=header_post)
    result_post = response_post_to_sheet.json()
    print(result_post)