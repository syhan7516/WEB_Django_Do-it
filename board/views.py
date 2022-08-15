from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('board/index')

def first(request):
    return HttpResponse('1')

def second(request):
    return HttpResponse('2')