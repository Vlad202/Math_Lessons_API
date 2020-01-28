from django.urls import path, include
from adminPanel import views

urlpatterns = [
    #local path
    path('', views.UsersListView.as_view()),
    #ban system
    path('users/ban/give/', views.GiveBanView.as_view()),
    #create
    path('themes/create/', views.CreateThemeView.as_view()),
    path('themes/<str:theme>/subtopic/create/', views.CreateTopicView.as_view()),
    path('themes/subtopics/<str:subtopic>/test/create/', views.CreateTestView.as_view()),
    #get
    path('themes/all/', views.ThemeListView.as_view()),
    path('themes/subtopics/get/<str:theme>/', views.CreateTopicView.as_view()),
    path('themes/subtopics/<str:subtopic>/tests/', views.TestView.as_view()),
    #edit
    path('themes/<str:theme>/edit/', views.EditThemeView.as_view()),
    path('themes/subtopics/test/<int:id>/edit/', views.EditTestView.as_view()),
    path('themes/subtopics/<str:subtopic>/edit/', views.EditSubtopicView.as_view()),
    #delete
    path('themes/<str:theme>/delete/', views.DeleteThemeView.as_view()),
    path('themes/subtopics/<str:subtopic>/delete/', views.DeleteThemeView.as_view()),
    path('themes/subtopics/test/<int:id>/delete/', views.EditTestView.as_view()),
]