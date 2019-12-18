from django.urls import path, include
from adminPanel import views

urlpatterns = [
    path('', views.UsersListView.as_view()),
    path('users/ban/give/', views.GiveBanView.as_view()),
]