from rest_framework import serializers

from core.models import Places


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Places
        fields = ('id', 'name', 'category', 'city', 'country', 'address', 'lat', 'lng')

        def create(self, validated_data):
            place = Places(
                id=validated_data['id'],
                name=validated_data['name'],
                category=validated_data['category'],
                city=validated_data['city'],
                country=validated_data['country'],
                address=validated_data['address'],
                lat=validated_data['lat'],
                lng=validated_data['lng'],
            )

            place.save()

            return place
