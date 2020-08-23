from rest_framework import serializers

from core.models import Pictures


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pictures
        fields = ('place', 'picture')
