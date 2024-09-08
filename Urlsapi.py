from rest_framework import routers
from .Viewsets import VideogameViewSet

router = routers.DefaultRouter()

router.register('', VideogameViewSet, 'videogames')

urlpatterns = router.urls
