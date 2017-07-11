import socket
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
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.err, msg):
        print("Failed to create socket. Error code: " + str(msg[0]) + ", Error message " + str(msg[1]))
        sys.exit()

    try:
        remote_ip = socket.gethostbyname('api.openweathermap.org')
    except socket.gaierror:
        print('Could not resolve hostname. Exiting')
        sys.exit()

    s.connect((remote_ip, 80))

    message = "GET /data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key + "&units=imperial HTTP/1.1\r\nhost: api.openweathermap.org\r\n\r\n"
    try:
        b = message.encode('utf-8')
        s.sendall(b)
    except socket.error:
        print('Failed to send request, exiting')
        sys.exit()

    reply = s.recv(4096)

    reply = reply.decode('utf-8')

    jsonString = reply[reply.index('{') : len(reply)]

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

def get_meme_name(api_key, lat, lon):
    condition = get_condition(api_key, lat, lon)
    conn = sqlite3.connect('../weathermeme_engine/db/memes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ' + condition)
    condition += str(random.randrange(1, len(c.fetchall())+1))
    c.close()
    conn.close()
    return condition

def get_condition(api_key, lat, lon):
    weather_info = get_weather_info(api_key, lat, lon)
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
