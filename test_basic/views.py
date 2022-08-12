from django.shortcuts import render

# HttpResponse 클래스 사용을 위한 import
from django.http import HttpResponse

# test_basic_function 정의
def test_basic_function(request):
    # HttpResponse : 페이지 요청에 대한 응답을 위해 사용하는 장고 클래스
    return HttpResponse('test_basic_function')