from rest_framework import serializers 
from .models import Videogame


class VideogameSerializer(serializers.ModelSerializer):
    """""
    This class will manage serialization and deserialization
    instructions from a Json format
    """""
    
  class Meta:
        model = Videogame()
        fields = ("id",
                  "title",
                  "creator",
                  "genre",
                  "description",
                  "published_date",
                  "steam_price")
      
        read_only_fields = (fields)
