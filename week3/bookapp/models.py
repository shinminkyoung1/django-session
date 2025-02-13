from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)       # 제목
    author = models.CharField(max_length=200)      # 저자
    isbn = models.BigIntegerField()                # 책 번호
    publication_date = models.DateField()          # 출판일
    available = models.BooleanField(default=True)  # 열람 가능 여부

    def __str__(self):
        return self.title
    

    