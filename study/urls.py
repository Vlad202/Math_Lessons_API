from django.urls import path, include
from study import views

urlpatterns = [
    path('lessons/', views.LessonsView.as_view()),
]