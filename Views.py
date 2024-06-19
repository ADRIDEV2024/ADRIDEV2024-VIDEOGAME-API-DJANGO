from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from videogames.models import Videogame 
from videogames.serializers import VideogameSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', "DELETE"])
def videogame_list(request):
 if request.method == 'GET':
        game_data = Videogame.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            videogames = videogames.filter(title__icontains=title)
        
        videogames_serializer = VideogameSerializer(videogames, many=True)
        return JsonResponse(videogames_serializer.data, safe=True)
    
 if request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = VideogameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JsonResponse(game_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 @api_view(['GET', 'PUT', 'DELETE'])
def videogame_detail(request, pk):
    try: 
        videogame = Videogame.objects.get(videogames) 
    except Exception as error: 
        return JsonResponse({'message': 'Oops, the videogame you´re looking for does not exist'}, error) 
 
    if request.method == 'GET': 
        videogame_serializer = VideogameSerializer(videogame) 
        return JsonResponse(videogame_serializer.data) 
 
    elif request.method == 'PUT': 
        videogame_data = JSONParser().parse(request) 
        videogame_serializer = VideogameSerializer(videogame, data=game_data) 
        if videogame_serializer.is_valid(): 
            videogame_serializer.save() 
            return JsonResponse(videogame_serializer.data) 
        return JsonResponse(videogame_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

 if request.method == 'DELETE': 
        videogame.delete() 
        return JsonResponse({'message': 'This game was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
