from rest_framework import serializers
from django.contrib.auth import get_user_model
UserModel = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username", "first_name", "last_name", "email", "is_active")