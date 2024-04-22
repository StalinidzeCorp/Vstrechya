from django.urls import path

from .views import MuseumViewSet, MuseumList

urlpatterns = [
    path('museum/', MuseumList.as_view(), name='museum'),
    path('museum/<int:id>', MuseumViewSet.as_view(), name='museum'),
]