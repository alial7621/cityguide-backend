from rest_framework import serializers

from core.models import Comments


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ('text', 'rate', 'place',)

