import socket
import sys
import json
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
        s.sendall(message)
    except socket.error:
        print('Failed to send request, exiting')
        sys.exit()

    reply = s.recv(4096)

    jsonString = reply[reply.index('{') : len(reply)]

    return json.loads(jsonString)

def get_response(api_key, lat, lon):
    response = {}
    weather_info = get_weather_info(api_key, lat, lon)
    response['meme_code'] = get_meme_code(weather_info)
    response['meme_location'] = 'http://andrewbevelhymer.com/weathermeme/meme/' + response['meme_code'] + '.png'
    response['weather_info'] = weather_info

    return json.dumps(response)

# Method that returns the 'meme_code' (filename)
# of the meme. This is the main algorithm that
# is pretty crappy right now. This is the part that
# needs to be improved the most in order for the api
# to actually become worthwhile. I'm open to pull
# requests if you are reading this and have ideas
def get_meme_code(weather_info):
        rand = random.randint(1, 6)

        main = weather_info['main']
        wind = weather_info['wind']

        if wind['speed'] > WIND_TRESHOLD:
                result = "wind" + str(rand)
        elif main['temp'] > HOT_TRESHOLD:
            result = "hot_weather" + str(rand)
        elif main['temp'] < COLD_TRESHOLD:
            result = "cold_weather" + str(rand)
        elif main['temp'] < CHILLY_TRESHOLD:
            result = "chilly" + str(rand)
        else:
            result = "neutral" + str(rand)

        return result
