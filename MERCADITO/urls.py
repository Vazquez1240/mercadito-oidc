from django.contrib import admin
from django.urls import path, include
from apirest.views import callback

urlpatterns = [
    path('dadmin/', admin.site.urls),
    path('rest/v1/', include('apirest.urls', namespace='apirest')),
    path('callback/', callback, name='callback'),
    path('rest/v1/auth/', include('rest_framework.urls'), name="rest_framework"),
]
