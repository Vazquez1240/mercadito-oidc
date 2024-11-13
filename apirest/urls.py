from django.urls import path, include
from rest_framework import routers

drf_router = routers.DefaultRouter()

app_name = 'apirest'

urlpatterns = [
    path('users/', include('users.urls')),
    path('', include(drf_router.urls)),
]

urlpatterns += drf_router.urls