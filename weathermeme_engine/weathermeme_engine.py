import requests
import sys
import json
import sqlite3
import random

HOT_TRESHOLD = 80
COLD_TRESHOLD = 40
CHILLY_TRESHOLD = 60
WIND_TRESHOLD = 20
RAIN_CODE = 500
SNOW_CODE = 600
THUNDERSTORM_CODE = 200

def get_weather_info(api_key, lat, lon):
    jsonString = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + api_key + '&units=imperial').text

    return json.loads(jsonString)

def get_owm_weather_id(weather_info):
    weather_list = weather_info['weather']
    id_list = []
    for info in weather_list:
        id_list.append(info['id'])

    return id_list

def get_temp(weather_info):
    return weather_info['main']['temp']

def get_wind_speed(weather_info):
    return weather_info['wind']['speed']

# This should be the entry point,
# returns json of all the data, including
# the location of the meme
def get_data(api_key, lat, lon):
    data = {}
    weather_info = get_weather_info(api_key, lat, lon)
    data['meme_name'] = get_meme_name(weather_info)
    data['meme_location'] = 'http://andrewbevelhymer.com/weathermeme/memes/' + data['meme_name'] + '.png'
    data['weather_info'] = weather_info
    return json.dumps(data)

def get_meme_name(weather_info):
    condition = get_condition(weather_info)
    conn = sqlite3.connect('../weathermeme_engine/db/memes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ' + condition)
    condition += str(random.randrange(1, len(c.fetchall())+1))
    c.close()
    conn.close()
    return condition

# This is the algorithm for generating the condition
def get_condition(weather_info):
    owm_weather_id_list = get_owm_weather_id(weather_info)

    temp = get_temp(weather_info)
    wind_speed = get_wind_speed(weather_info)

    for weather_id in owm_weather_id_list:
        if weather_id > 600 and weather_id < 700:
            return 'snow'
        elif weather_id > 500 and weather_id < 600 or weather_id > 200 and weather_id < 400:
            return 'rain'

    if wind_speed > WIND_TRESHOLD:
        return 'windy'
    elif temp < COLD_TRESHOLD:
        return 'cold'
    elif temp < CHILLY_TRESHOLD:
        return 'chilly'
    elif temp < HOT_TRESHOLD:
        return 'neutral'
    elif temp >= HOT_TRESHOLD:
        return 'hot'

    return 'err'
