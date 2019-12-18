from rest_framework import serializers
from django.contrib.auth import get_user_model
from adminPanel.models import BanUserModel
UserModel = get_user_model()

class UsersListSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username", "first_name", "last_name", "email",)

class BanUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanUserModel
        fields = ("__all__")