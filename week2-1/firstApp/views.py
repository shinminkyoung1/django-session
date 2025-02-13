from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>🦁</h1>")

def displayNow(request):
    dt = datetime.datetime.now()
    s = "<b>현재 시각: </b>" + str(dt)
    return HttpResponse(s)