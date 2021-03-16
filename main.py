from fastapi.logger import logger as fastapi_logger
import requests
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import logging
import os
import time
app = FastAPI()

# MODELS


class Weather(BaseModel):
    city_name: str


# MIDDLEWARE
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://192.168.1.3:8080/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES/ENDPOINTS


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/city/")
def current_city_temp(data: Weather):
    logging.info(data)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(
        data.city_name, os.environ.get('API_KEY'))
    data = requests.get(url).json()
    current_temp = data['main']['temp']
    current_temp = round(current_temp - 273.15)
    # this will return something like 'clear skies
    description = data['weather'][0]['description']
    feels_like = round(data['main']['feels_like'] - 273.15)
    time_now = data['dt']
    time_now = time.ctime(time_now)
    return {"time": time_now, "current_temp": current_temp, "feels_like": feels_like, "description": description}
