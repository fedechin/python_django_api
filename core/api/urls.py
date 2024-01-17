from django.urls import path
from api import views

urlpatterns = [
    path('chucknorris.io/jokes/random', views.JokeViewSet),
]
