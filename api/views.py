from rest_framework import generics
from api.serializers import LessonArticleDetailSerializer, LessonArticleListSerializer
from api.models import LessonArticle
from api.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

class CreateArticle(generics.CreateAPIView):
    serializer_class = LessonArticleDetailSerializer
    permission_classes = (IsAdminUser, )

class ArticlesList(generics.ListAPIView):
    serializer_class = LessonArticleListSerializer
    queryset = LessonArticle.objects.all()
    permission_classes = (IsAuthenticated, )

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonArticleDetailSerializer
    queryset = LessonArticle.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser, )