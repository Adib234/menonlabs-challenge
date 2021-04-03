import requests
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import plotly.graph_objects as go
import os
import time
import base64


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
def current_weather(data: Weather):
    print(data)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'.format(
        data.city_name, os.environ.get('API_KEY'))
    data = requests.get(url).json()
    current_temp = data['main']['temp']
    current_temp = round(current_temp - 273.15)
    # this will return something like 'clear skies
    description = data['weather'][0]['description']
    feels_like = round(data['main']['feels_like'] - 273.15)

    min_temp = data['main']['temp_max']
    min_temp = round(min_temp - 273.15)
    max_temp = data['main']['temp_max']
    max_temp = round(max_temp - 273.15)
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    time_now = data['dt']
    time_now = time.ctime(time_now)
    return {"time": time_now, "current_temp": current_temp, "feels_like": feels_like, "description": description,
            "min_temp": min_temp, "max_temp": max_temp, "humidity": humidity, "Pressure": pressure}


@app.post('/forecast/{forecast_filter}')
def city_forecast(forecast_filter: str, data: Weather):
    print(data)
    print(forecast_filter)
    url = 'http://api.openweathermap.org/data/2.5/forecast?q={0}&appid={1}'.format(
        data.city_name, os.environ.get('API_KEY'))
    kelvins = -273.15
    data = requests.get(url).json()
    times = []
    temp = []
    temp_min = []
    temp_max = []
    for item in data['list']:
        times.append(time.ctime(item['dt']))
        temp.append(round(item["main"]['temp']+kelvins))
        temp_max.append(round(item["main"]['temp_max']+kelvins))
        temp_min.append(round(item["main"]['temp_min']+kelvins))

    fig = go.Figure()
    # Create and style traces
    title = ''
    if forecast_filter == '' or forecast_filter == 'All':
        fig.add_trace(go.Scatter(x=times, y=temp, name='Temperature',
                                 line=dict(color='firebrick', width=4)))
        fig.add_trace(go.Scatter(x=times, y=temp_max, name='Max temp.',
                                 line=dict(color='firebrick', width=4, dash="dash")))
        fig.add_trace(go.Scatter(x=times, y=temp_min, name='Min temp.',
                                 line=dict(color='firebrick', width=4, dash='dot')))
        title = 'Temperatures for normal, min, and max forecasted'
    elif forecast_filter == 'Maximum':

        fig.add_trace(go.Scatter(x=times, y=temp_max, name='Maximum',
                                 line=dict(color='firebrick', width=4)))
        title = 'Temperatures for max forecasted'
    elif forecast_filter == 'Normal':
        fig.add_trace(go.Scatter(x=times, y=temp_max, name='Normal',
                                 line=dict(color='firebrick', width=4)))
        title = 'Temperatures for normal forecasted'
    else:
        fig.add_trace(go.Scatter(x=times, y=temp_min, name='Minimum',
                                 line=dict(color='firebrick', width=4)))
        title = 'Temperatures for min forecasted'

        # Edit the layout
    fig.update_layout(title=title,
                      xaxis_title='Time',
                      yaxis_title='Temperature (degrees C)')
    fig.write_image("../images/fig1.webp")
    with open("../images/fig1.webp", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string
