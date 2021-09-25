from django.conf import settings
from django.urls import path
from rest_framework import routers
from .views import *
from rest_framework.routers import DefaultRouter

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.


router = DefaultRouter()
# router = routers.SimpleRouter(trailing_slash=True)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
#router.register(r'pokemons', Pokemon)
urlpatterns = [
path('evolutions/<pk>/', Evolution.get_service),
path('pokemons/<pk>/', Pokemon.get_service),
] + router.urls
