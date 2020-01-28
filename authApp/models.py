from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailVerification(models.Model):
    ip = models.CharField(max_length=128, default="")
    email_hash = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    def __str__(self):
        return self.username

class UserToken(models.Model):
    token = models.CharField(max_length=128)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

class UserAgent(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, default="")
    ipAgent = models.CharField(max_length=128, verbose_name="ip_agent")
    email = models.CharField(max_length=128, verbose_name="ban_email")
    def __str__(self):
        return self.email