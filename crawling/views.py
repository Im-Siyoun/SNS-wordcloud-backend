from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json

@method_decorator(csrf_exempt, name='dispatch')
def crawling(request):
    print(request)
    temp = json.loads(request.body)
    searching_keyword = temp['keyword']
    print(searching_keyword, temp, sep="\n")
    return HttpResponse(searching_keyword)
