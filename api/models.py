from django.db import models
from django.contrib.auth import get_user_model
# Fix: username length is too small,email must be unique
from django.contrib.auth.models import User, models
User._meta.local_fields[1].__dict__['max_length'] = 75
User._meta.local_fields[4].__dict__['_unique'] = True
User = get_user_model()

class LessonArticle(models.Model):
    header = models.CharField(verbose_name='header', unique=True, db_index=True, max_length=128)
    body = models.TextField(verbose_name='body')

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)