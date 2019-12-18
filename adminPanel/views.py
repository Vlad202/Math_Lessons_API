from rest_framework import generics
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from adminPanel.serializers import UsersListSetSerializer, BanUserSerializer
from adminPanel.models import BanUserModel
from authApp.models import UserAgent

class UsersListView(generics.ListAPIView):
    serializer_class = UsersListSetSerializer
    queryset = User.objects.all()

class GiveBanView(APIView):
    serializer = BanUserSerializer
    def post(self, request):
        if request.method == 'POST':
            # find_ban_user = BanUserModel.objects.get(email=request.POST['email'])
            # if find_ban_user is None:
            bad_user_email = UserAgent.objects.get(email=request.POST['email'])
            if bad_user_email is not None:
                banned_user = BanUserModel.objects.create(
                    ip_agent = bad_user_email.ipAgent,
                    email = bad_user_email.email,
                )
                banned_user.save()
                User.objects.get(email=request.POST['email']).delete()
                return Response({'user': 'is banned'})
            # return Response({'error': 'unknown user'})
            return Response({'error': 'user is alredy banned'})
        return Response({'error': 'method not allowed'})