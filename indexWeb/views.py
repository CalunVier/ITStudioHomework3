from django.shortcuts import render, redirect
from indexWeb.WeatherForecast.weather import get_forecast_normal
from indexWeb.ZhihuDudu.zhidududu import get_latest
from urllib import request, parse
import json
# Create your views here.


# Index
def index(request):
    location_weather_forecast = get_forecast_normal('auto_ip')
    if request.method == 'POST':
        print('post'+request.POST.get('slocation'))
        if request.POST.get('s') and request.POST.get('slocation'):
            location_weather_forecast = get_forecast_normal(request.POST.get('slocation'))
    zhihu = get_latest()
    return render(request, 'Index.html',
                  {
                      'forecast': location_weather_forecast['HeWeather6'][0],
                      'zhihu': zhihu
                  })


def news(req, nid):
    njs = json.loads(request.urlopen(request.Request('https://news-at.zhihu.com/api/4/news/'+nid)).read())
    if 'body' in njs:
        return render(req, "news.html", {'njs': njs})
    else:
        return redirect(njs['share_url'])
