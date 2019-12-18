from django.contrib import admin
from authApp.models import UserToken, EmailVerification, UserAgent

admin.site.register(UserToken)
admin.site.register(EmailVerification)
admin.site.register(UserAgent)