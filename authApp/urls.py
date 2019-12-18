from django.urls import path, include
from authApp import views

urlpatterns = [
    path('signup/', views.CreateUserView.as_view()),
    path('signin/', views.SinginUserView.as_view()),
    path('signup/verification-email/<str:email_hash>', views.EmailVerificationView.as_view())
]