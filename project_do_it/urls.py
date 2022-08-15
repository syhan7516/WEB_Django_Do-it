from django.contrib import admin

# 기본 urls path에서 url 분리를 위해 include 추가
from django.urls import path
from django.urls import include

# test_basic App url 추가를 위한 import
from test_basic import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # test_baisc App path 접근 → views파일의 test_function 리턴
    path('test_basic/',views.test_basic_function),

    # test_separation App관련 모든 path 접근 → test_separation App의 urls file에서 처리
    path('test_separation/',include('test_separation.urls')),

    # board App path 접근 → board App의 urls file에서 처리
    path('board/',include('board.urls'))
]