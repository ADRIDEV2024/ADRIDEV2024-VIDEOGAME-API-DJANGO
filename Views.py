from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from videogames.models import Videogame 
from videogames.serializers import VideogameSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def videogame_list(request):
 if request.method == 'GET':
        tutorials = Videogame.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            videogames = videogames.filter(title__icontains=title)
        
        videogames_serializer = VideogameSerializer(videogames, many=True)
        return JsonResponse(videogames_serializer.data, safe=True)
    
 elif request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = VideogameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse(game_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)