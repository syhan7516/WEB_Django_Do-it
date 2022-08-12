from django.shortcuts import render
# HTTPResponse 클래스를 사용하기 위해 import
from django.http import HttpResponse

def test_function(request):
    # HTTPResponse : 페이지 요청에 대한 응답할 때 사용하는 장고 클래스
    return HttpResponse('tset_function')