from rest_framework import routers
from .Viewsets import VideogameViewSet

router = routers.DefaultRouter()

router.register('Djangoapi/videogames', VideogameViewSet, 'videogames')

urlpatterns = router.urls
