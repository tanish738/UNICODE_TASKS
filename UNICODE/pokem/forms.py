from django.forms import ModelForm, fields
from .models import *



class Pokem(ModelForm):
    class Meta:
        model=Pokemon
        fields='__all__'

class PokemonNames(ModelForm):
    class Meta:
        model=Pokemons
        fields='__all__'