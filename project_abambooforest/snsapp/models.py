from statistics import mode
from django.db import models

# 게시물 모델
class Post(models.Model):
    titile = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)