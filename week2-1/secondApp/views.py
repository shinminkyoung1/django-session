from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayQuote(request):
    s = "<h1>소크라테스: 너 자신을 알라</h1>"
    return HttpResponse(s)