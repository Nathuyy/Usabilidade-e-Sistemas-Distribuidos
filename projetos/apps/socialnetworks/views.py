from django.shortcuts import render
from rest_framework import viewsets
from .models import Socialnetwork
from .serializer import SocialNetworkSerializer

# Create your views here.
class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = Socialnetwork.objects.all()
    serializer_class = SocialNetworkSerializer 