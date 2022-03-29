from django.contrib import admin
from django.urls import path
from .views import MovieViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('users', UserViewSet)
urlpatterns = router.urls
