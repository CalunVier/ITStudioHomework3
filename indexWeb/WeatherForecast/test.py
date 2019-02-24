from urllib import request,parse
from indexWeb.WeatherForecast.weather import get_now, get_forecast_normal
data = {'location': '百度', 'key': '28144cfd30634d398f18240a8629a201'}
data = parse.urlencode(data)
req = request.Request("https://free-api.heweather.net/s6/weather/now?"+data)
res = request.urlopen(req)
res = res.read()
print(get_forecast_normal('北京'))
