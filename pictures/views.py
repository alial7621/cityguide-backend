from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Pictures, MyUser
from pictures.serializers import PictureSerializer


class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    queryset = Pictures.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload')
    def upload_image(self, request):
        # user = MyUser.objects.get(user=self.request.user)
        serializer = self.get_serializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get_queryset(self):
        queryset = Pictures.objects.all()
        place = self.request.query_params.get('place', None)
        if place is not None:
            queryset = queryset.filter(place__id=place).order_by('-time')
        return queryset

