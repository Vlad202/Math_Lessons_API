from django.urls import path, include
from userClientSide import views

urlpatterns = [
    path('', views.ProfileView.as_view()),
]