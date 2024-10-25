from django.db import models

# 회원정보 관련 모델 스키마 정의 (스키마 : 저장할 데이터의 구조를 강제하는 시스템적인 틀)
# 장고에서는 코드 개발시 모델을 객체형식으로 다루게 됨으로 sql를 모르더라도 개발 가능
# 하지만 실제적으로 구동시에는 장고가 자체적으로 table형식으로 변환해서 저장 ORM(Object Relational Mapping)
class Member(models.Model): # class 클래스명(대문자로 써야함)
  # username이라는 field에 문자열 30글자까지만 입력받을 수 있는 구조 강제처리
  # max_length로 지정가능한 최대 문자 갯수는 255
  # models.CharField(max_length=30) 문자를 30글자 지정
  username = models.CharField(max_length=30) 
  age = models.IntegerField(null=True)
  date = models.DateField(null=True)
  
  def __str__(self):
    return f"{self.id}: {self.username} ({self.age}세) , 가입날짜: {self.date}"
  
  