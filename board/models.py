from django.db import models

class Board(models.Model):
    id = models.AutoField(primary_key=True)     # 기본 키 (자동으로 증가하는 정수형 필드)
    title = models.CharField(max_length=20)     # 제목
    content = models.TextField(max_length=100)  # 내용
    writer = models.CharField(max_length=10)    # 작성자