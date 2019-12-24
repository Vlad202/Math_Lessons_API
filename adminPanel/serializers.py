from rest_framework import serializers
from django.contrib.auth import get_user_model
from adminPanel.models import BanUserModel, GlobalThemeModel, SubtopicModel, TestModel
UserModel = get_user_model()

class CreateThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalThemeModel
        fields = ("__all__")

class CreateTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtopicModel
        fields = ("__all__")

class UsersListSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("username", "first_name", "last_name", "email",)

class BanUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BanUserModel
        fields = ("__all__")

class ThemeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalThemeModel
        fields = ("__all__")

class CreateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ("__all__")