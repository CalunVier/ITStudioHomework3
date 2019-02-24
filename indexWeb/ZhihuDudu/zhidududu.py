from urllib import request
import json


def get_latest():
    return json.loads(request.urlopen(request.Request('https://news-at.zhihu.com/api/4/news/latest')).read())


def read_article(id):
    return json.loads(request.urlopen(request.Request('https://news-at.zhihu.com/api/4/news/'+id)).read())