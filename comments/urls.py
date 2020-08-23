from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comments import views

router = DefaultRouter()
router.register('add', views.CommentViewSet)

app_name = 'comment'

urlpatterns = [
    path('', include(router.urls)),
]
