from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request) :
    return HttpResponse("main 페이지 입니다")

