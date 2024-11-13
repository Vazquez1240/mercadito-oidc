from apirest.urls import drf_router
from .viewsets import UserViewSet

urlpatterns = [

]
drf_router.register(r'users', UserViewSet, basename='users')