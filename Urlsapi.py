from rest_framework import routers
from .Viewsets import VideogameViewSet

router = routers.DefaultRouter()

router.register('api/videogames', VideogameViewSet, name= 'videogames')

urlpatterns = router.urls
