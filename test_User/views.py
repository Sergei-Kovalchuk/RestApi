from .serializers import CreateUserSerializer
from .models import Create

from rest_framework.viewsets import ViewSet, ModelViewSet

class UserViewSet(ModelViewSet):
    queryset = Create.objects.all()
    serializer_class = CreateUserSerializer



