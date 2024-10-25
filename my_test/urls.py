from django.contrib import admin
from django.urls import path, include

# 해당 urls는 해당 프로젝트 안쪽에 있는 개별적인 앱의 url정보값을 불러와서 연결해주는 역할
urlpatterns = [
    path('admin/', admin.site.urls),
    # 순서0 - path로 2개 경로를 이어붙임: 기본 url뒤에 member_app에 등록된 urls가져와서 연결
    path('', include('member_app.urls'))
]
