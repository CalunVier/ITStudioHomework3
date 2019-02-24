from urllib import request, parse
import json


# https://www.heweather.com/documents/api/s6/weather-now
def get_now(locat):
    data = parse.urlencode({'location': locat, 'key': '28144cfd30634d398f18240a8629a201'})
    req = request.Request("https://free-api.heweather.net/s6/weather/now?" + data)
    return json.loads(request.urlopen(req).read().decode('utf-8'))


# https://www.heweather.com/documents/api/s6/weather-all
def get_forecast_normal(locat):
    data = parse.urlencode({'location': locat, 'key': '28144cfd30634d398f18240a8629a201'})
    req = request.Request('https://free-api.heweather.net/s6/weather?' + data)
    return json.loads(request.urlopen(req).read().decode('utf-8'))


# https://www.heweather.com/documents/api/s6/weather-hourly
def get_forecast_hour(locat):
    data = parse.urlencode({'location': locat, 'key': '28144cfd30634d398f18240a8629a201'})
    req = request.Request('https://free-api.heweather.net/s6/weather/hourly?' + data)
    return json.loads(request.urlopen(req).read().decode('utf-8'))


# https://www.heweather.com/documents/api/s6/lifestyle
def get_life_suggest(locat):
    data = parse.urlencode({'location': locat, 'key': '28144cfd30634d398f18240a8629a201'})
    req = request.Request('https://free-api.heweather.net/s6/weather/lifestyle?' + data)
    return json.loads(request.urlopen(req).read().decode('utf-8'))

