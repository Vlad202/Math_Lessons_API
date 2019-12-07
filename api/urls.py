from django.urls import path, include
from api import views

urlpatterns = [
    path('articles/create/', views.CreateArticle.as_view()),
    path('all/', views.ArticlesList.as_view()),
    path('lesson/detail/<int:pk>', views.ArticleDetail.as_view())
]