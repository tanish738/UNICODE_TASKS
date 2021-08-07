from django.db import models




# Create your models here.



class Pokemon(models.Model):
    CATEGORY = (
			('normal','normal'),
            ('fighting','fighting'),
            ('flying','flying'),
            ('poison','poison'),
            ('ground','ground'),
            ('rock','rock'),
            ('bug','bug'),
            ('ghost','ghost'),
            ('steel','steel'),
            ('fire','fire'),
            ('water','water'),
            ('grass','grass'),
            ('electric','electric'),
            ('psychic','psychic'),
            ('icedragon','icedragon'),
            ('darkfairy','darkfairy'),
            ('unknown','unknown'),
            ('shadow','shadow'),
			) 
    category=models.CharField(max_length=200,choices=CATEGORY)


class Pokemons(models.Model):
    name=models.CharField(max_length=100)

class PokemonData(models.Model):
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    u_name=models.CharField(max_length=200,null=True)
    height=models.IntegerField(null=True)
    weight=models.CharField(max_length=200, null=True)
    move=models.CharField(max_length=1000,null=True)
    abilities=models.CharField(max_length=300,null=True)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.u_name
    def isExists(self):
        if PokemonData.objects.filter(u_name=self.u_name):
            return True
        else:
            return False
    