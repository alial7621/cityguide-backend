from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from comments.serializers import CommentSerializer
from core.models import Comments


class CommentViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comments.objects.all()
        place = self.request.query_params.get('place', None)
        if place is not None:
            queryset = queryset.filter(place__id=place).order_by('-time')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
