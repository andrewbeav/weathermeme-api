import weathermeme_engine
import sys

def write_result(api_key, lat, lon):
    f = open('weathermeme_result.json', 'w')
    f.write(weathermeme_engine.get_response(api_key, lat, lon))

write_result(sys.argv[1], sys.argv[2], sys.argv[3])
