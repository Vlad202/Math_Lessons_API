from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class LessonArticle(models.Model):
    header = models.CharField(verbose_name='header', unique=True, db_index=True, max_length=128)
    body = models.TextField(verbose_name='body')

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)