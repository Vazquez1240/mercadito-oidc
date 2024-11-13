from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dadmin/', admin.site.urls),
    path('rest/v1', include('apirest.urls', namespace='apirest')),
    path('rest/v1/auth', include('rest_framework.urls'), name="rest_framework"),
]
