from rest_framework import routers
from .Viewsets import VideogameViewSet

router = routers.DefaultRouter()

router.register('api/videogames', VideogameViewSet, 'videogames')

urlpatterns = router.urls
