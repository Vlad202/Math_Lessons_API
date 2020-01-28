from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from authApp.models import UserToken
from adminPanel.permisions import user_is_auth
from django.core import serializers
from userClientSide.serializers import ProfileSerializer

class ProfileView(APIView):
    def get(self, request):
        token = request.COOKIES["Token"]
        if user_is_auth(token):
            user = UserToken.objects.get(token=token).user
            serializer = ProfileSerializer(user)
            return Response(serializer.data, status=200)
        else:
            return Response({
                'status': 'Bad request',
                'message': 'Account could not be created with received data.'
            }, status=400)