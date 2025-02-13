from django.shortcuts import render
from django.http import HttpResponse  # 추가한 라인

# Create your views here.
def display(request):
    return HttpResponse("<h1>첫 장고앱 생성 완료 Vv</h1>")