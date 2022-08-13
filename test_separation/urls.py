from django.urls import path

# 해당 App url 추가를 위한 import
from . import views

urlpatterns = [
    # 해당 App대한 test_separation/ 접근 → views파일의 index함수 리턴
    path('',views.index),
    # 해당 App대한 test_separation/first 접근 → views파일의 first함수 리턴
    path('first',views.first),
    # 해당 App대한 test_separation/second 접근 → views파일의 second함수 리턴
    path('second',views.second),
]
