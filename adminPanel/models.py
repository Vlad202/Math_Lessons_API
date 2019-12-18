from django.db import models

class BanUserModel(models.Model):
    ip_agent = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)