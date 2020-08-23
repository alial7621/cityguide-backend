from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pictures import views

router = DefaultRouter()
router.register('add', views.PictureViewSet)

app_name = 'picture'

urlpatterns = [
    path('', include(router.urls)),
]
