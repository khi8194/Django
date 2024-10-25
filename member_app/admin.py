from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
  list_display = ('username','age','date')

# register 메서드를 이용하여 admin 페이지에서 Member 모델을 등록시 2번째 인수로 위에서 정의한 클래스 같이 전달
admin.site.register(Member,MemberAdmin)

