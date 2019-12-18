from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api/', include('api.urls')),
    path('api/v1/auth/', include('authApp.urls')),
    path('api/v1/admin/', include('adminPanel.urls')),
]
