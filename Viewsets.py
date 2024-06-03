from .models import Videogame
from rest_framework import viewset, permissions
from .serializers import VideogameSerializer

class VideogameViewSet(viewset.ModelViewSet):
    """""
    This class is for retrieve the data we want to query,only for 
    authenticated people
    """""
    queryset = Videogame.objects.all()
    permissions = [permissions.IsAuthenticated]
    serializer_class = VideogameSerializer
