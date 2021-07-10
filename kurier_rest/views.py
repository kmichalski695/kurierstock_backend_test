from rest_framework import viewsets, permissions
from .serializers import RowerSerializer
from .models import Rower


class RowerViewSet(viewsets.ModelViewSet):
    serializer_class = RowerSerializer
    queryset = Rower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
