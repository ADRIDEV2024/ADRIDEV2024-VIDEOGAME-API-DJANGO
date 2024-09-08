from rest_framework import serializers 
from .models import Videogame


class VideogameSerializer(serializers.ModelSerializer):
    
    
  class Meta:
      
        model = Videogame
        fields = ("id",
                  "title",
                  "creator",
                  "genre",
                  "description",
                  "published_date",
                  "steam_price")
      
        
