from django.urls import path
from . import views

urlpatterns = [
    path('',views.poketypes),
    path('pokemon/<str:pk>/',views.pokemonspoketypes,name="pokemon"),
    path('about/',views.about,name="about"),
    path('poke/<str:pk>/',views.pokemonhtml,name="home"),
    path('name/',views.pokemonhtml),
    path('data/',views.displaypokemon),
    path('maindata/',views.displaypokemon2),
    path('/<str:number>/',views.url,name="link"),
]
