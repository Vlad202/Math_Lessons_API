from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authApp.urls')),
    path('api/v1/admin/', include('adminPanel.urls')),
    path('api/v1/user/', include('userClientSide.urls')),
    path('api/v1/learning/', include('study.urls')),
]
