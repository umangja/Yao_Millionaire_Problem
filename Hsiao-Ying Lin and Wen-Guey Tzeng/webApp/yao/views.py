
from millionare.Algo2 import getricher
from django.shortcuts import render
from django.http import HttpResponse
import json

def checkrich(request):
    r=json.loads(request.body)
    x=int(r['x'])
    y=int(r['y'])
    result=getricher(x,y)
    return HttpResponse(json.dumps(result))

def home(request):
    return render(request, 'index.html')