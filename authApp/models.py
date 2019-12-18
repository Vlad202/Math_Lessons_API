from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailVerification(models.Model):
    ip = models.CharField(max_length=60, default="")
    email_hash = models.CharField(max_length=60)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class UserToken(models.Model):
    token = models.CharField(max_length=64)

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

class UserAgent(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, default="")
    ipAgent = models.CharField(max_length=128, verbose_name="ip_agent")
    email = models.CharField(max_length=128, verbose_name="ban_email")