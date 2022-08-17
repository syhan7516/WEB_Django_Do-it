from django.db import models

# 질문관련 모델 생성
class Question(models.Model):
    # 질문명에 대한 
    # → CharField : 글자 제한이 있는 필드 
    # → max_length : 속성 중 길이를 숫자로 명시 가능
    subject = models.CharField(max_length=200)

    # 내용에 대한
    # → TextField : 글자 제한이 없는 필드
    content = models.TextField()

    # 생성 시간에 대한
    # → DateTimeField : 날짜, 시간관련 필드
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    # 댓글과 이어진 질문에 대한
    # → ForeignKey : 외부 모델을 잇기위한 필드
    # → 외래 키의 속성 값으로 연결할 모델, 수정변경삭제의 경우 처리될 방법
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()