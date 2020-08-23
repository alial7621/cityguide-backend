from django.urls import path

from places import views

app_name = 'place'

urlpatterns = [
    path('add/', views.AddPlace.as_view(), name='add'),
]
