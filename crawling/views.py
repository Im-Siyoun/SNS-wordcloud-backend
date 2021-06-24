# -*- coding: utf-8 -*-
import base64
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from django.core.files import File
from django.http import JsonResponse
import json
from bs4 import BeautifulSoup as bs
from . crawling import maincrawling
from . wordcloud import cloud
from konlpy.tag import Okt

@api_view(['POST'])
@method_decorator(csrf_exempt, name='dispatch')
def crawling(request):
    temp = json.loads(request.body)
    searching_keyword = temp['keyword']
    html = maincrawling(searching_keyword)
    object = bs(html, 'html.parser')
    res = object.findAll('span', {"class":"a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7"})
    result = ''
    for i in res:
        result += i.text
    okt = Okt()
    result = okt.nouns(result)
    for i, v in enumerate(result):
        if len(v) < 2:
            result.pop(i)
    text = ''
    for i in result:
        text += i+' '
    result = cloud(text)
    with open('wordcloud.png', 'rb') as img:
        data = base64.b64encode(img.read())
    return JsonResponse({'data': data.decode()})