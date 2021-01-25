from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100, verbose_name="Текст")
    created_at = models.DateField(auto_now_add=True, verbose_name="Создана")
    is_closed = models.BooleanField(default=False, verbose_name="Закрыть")
    is_favorite = models.BooleanField(default=False, verbose_name="Приоритет")
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    desctiption = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    genre = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.DateField()
    date = models.DateField(auto_now_add=True)