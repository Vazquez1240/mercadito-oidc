from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
# from .permissions import IsAuthenticatedAndObjUserOrIsStaff
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework import exceptions

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    parser_classes = [JSONParser]
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        elif self.request.user.is_staff:
            return User.objects.all()
        elif self.request.user.is_authenticated:
            return User.objects.filter(pk=self.request.user.pk)
        else:
            raise exceptions.PermissionDenied('Forbidden')