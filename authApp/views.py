from rest_framework import generics
from authApp.serializers import CreateUserSerializer, SigninUserSerializer, EmailVerificationSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.views import APIView
from authApp.models import UserToken, EmailVerification, UserAgent
from rest_framework.response import Response
import hashlib
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()

class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = CreateUserSerializer


class EmailVerificationView(APIView):
    def get(self, request, email_hash):
        serializer = EmailVerificationSerializer

        email_vr_user = EmailVerification.objects.get(email_hash=email_hash)
        if email_vr_user is None:
            return Response({'error': 'unknown user'})
        else:
            user = UserModel.objects.create(
                username=email_vr_user.username,
                email=email_vr_user.email,
                first_name=email_vr_user.first_name,
                last_name=email_vr_user.last_name
            )
            user.set_password(email_vr_user.password)
            user.save()
            user_ip = UserAgent.objects.create(
                user=user,
                ipAgent=email_vr_user.ip,
                email=email_vr_user.email
            )
            user_ip.save()
            hash_token = email_vr_user.username + email_vr_user.password
            for i in range(1, 11):
                hash_token += '10'
                hash_token = hashlib.sha256(hash_token.encode('utf-8')).hexdigest()

            token = UserToken.objects.create(
                token=hash_token,
                user=UserModel.objects.get(username=email_vr_user.username)
            )
            token.save()
            email_vr_user.delete()
            return Response({'success': 'true'})


class SinginUserView(APIView):
    def post(self, request):
        serializer = SigninUserSerializer

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user.is_staff == True:
            token = UserToken.objects.get(user=user.id).token
            return Response({"user": "is staff", "token": token})

        if user is None:
            return Response(messages.error(request,'username or password not correct'))
        else:
            token = UserToken.objects.get(user=user.id).token
            return Response({"token": token})    

