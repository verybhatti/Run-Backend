

# Create your views here.
from rest_framework import viewsets
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404  
from .models import User
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)        