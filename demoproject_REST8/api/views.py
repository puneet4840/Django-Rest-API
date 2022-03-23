from django.shortcuts import render
from api.models import Student
from rest_framework import viewsets
from api.serializer import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly


# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]