from django.urls import path, include
from adminPanel import views

urlpatterns = [
    path('', views.UsersListView.as_view()),
    path('users/ban/give/', views.GiveBanView.as_view()),
    path('themes/create/', views.Createtheme.as_view()),
    path('themes/all/', views.ThemeListView.as_view()),
    path('themes/edit/<str:theme>/', views.EditThemeView.as_view()),
    path('themes/<str:theme>/', views.CreatetopicView.as_view()),
    path('themes/topics/<str:subtopic>/tests/', views.TestView.as_view()),
    path('themes/topics/test/<int:id>/edit/', views.EditTestView.as_view()),
    path('themes/topics/<str:subtopic>/edit/', views.EditSubtopicView.as_view()),
]