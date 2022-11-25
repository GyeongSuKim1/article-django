from django.db import models

# Create your models here.

class Article (models.Model):
    title = models.CharField("제목", max_length=35)
    content = models.CharField("내용", max_length=500)
    
    created_at = models.DateTimeField("게시글 등록 일자", auto_now_add=True)
    updated_at = models.DateTimeField("게시글 수정 일자", auto_now=True)
    
    def __str__(self):
        return f"{self.id} | 제목 : {self.title}"