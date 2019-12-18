from rest_framework import serializers
from api.models import LessonArticle

class LessonArticleDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = LessonArticle
        fields ='__all__'

class LessonArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonArticle
        fields = ('id', 'header', 'user')