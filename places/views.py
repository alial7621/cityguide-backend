from rest_framework import generics

from places.serializers import PlaceSerializer


class AddPlace(generics.CreateAPIView):
    """Add new place to database"""
    serializer_class = PlaceSerializer
