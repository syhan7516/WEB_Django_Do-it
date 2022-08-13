from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('test_separation_index')

def first(request):
    return HttpResponse('test_separation_first')

def second(request):
    return HttpResponse('test_separation_second')
