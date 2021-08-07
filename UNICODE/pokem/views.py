from django.shortcuts import redirect, render,HttpResponseRedirect
from django.http import HttpResponse, response
from .forms import *
from .models import *
import requests
import json
# Create your views here.
# 2 ND TASK
r=requests.get("https://pokeapi.co/api/v2/type/").json()
def about(request):
    poke={}
    pokemon_names=[]
    #print(r['results'])
    for result in r['results']:
        pokemon_names.append("'")
        pokemon_names.append(result['name'])
        pokemon_names.append("'")
        pokemon_names.append(":")
        for data in requests.get(result['url']).json()['pokemon']:
            pokemon_names.append(data['pokemon']['name'])
            pokemon_names.append(",")
        pokemon_names.append("\n")
    return HttpResponse(pokemon_names)







# 3RD TASK
def poketypes(request):
    form=Pokem()
    name=PokemonData.objects.all()
    if request.method=='POST':
        pk=request.POST['category']
        context={'form':form,'pk':pk,'name':name}
        return render(request,"poke.html",context)
        #return HttpResponseRedirect('poke/'+pk+'/')
    else:
        context={'form':form,'pk':"Hello",'name':name}
        return render(request,"poke.html",context)


def pokemonspoketypes(request,pk):
    name=[]
    final_pokemon_name=[]
    for result in r['results']:
            if result['name']==pk:
                for names in requests.get(result['url']).json()['pokemon']:
                    name.append(names['pokemon']['name'])
    if request.method=="POST":
        form=PokemonNames(request.POST)
        if request.POST['name'] not in name:
            details="You have not entered the right pokemon name please try again"
            url=""
            number=3
            context={"name":name,"pk":pk,"form":form,"details":details,"url":url,"number":number}
            return render(request,"pk.html",context)

        else:
            for result in r['results']:
                if result['name']==pk:
                    for names in requests.get(result['url']).json()['pokemon']:
                        if request.POST['name']==names['pokemon']['name']:
                            url=requests.get(names['pokemon']['url']).json()['sprites']['front_default']
                            number=url.split("/")[-1].split(".")[0]
                            print(url.split("/")[-1].split(".")[0])
                            details=request.POST['name']
                            context={"name":name,"pk":pk,"form":form,"details":details,"url":url,"number":number}
                            return render(request,"pk.html",context)
                            #return redirect(requests.get(names['pokemon']['url']).json()['sprites']['front_default'])
    else:
        print("f")
        form=PokemonNames()
        context={"name":name,"pk":pk,"form":form,"url":"www.google.com","number":3,"details":""}
        return render(request,"pk.html",context)



def pokemonhtml(request,pk):
    name=[]
    final_pokemon_name=[]
    for result in r['results']:
            if result['name']==pk:
                for names in requests.get(result['url']).json()['pokemon']:
                    name.append(names['pokemon']['name'])
                if request.method=="POST":
                    print(request.POST['pokemon'])
                    if request.POST['pokemon']  not in name:
                        print("f")
                        details="You have not entered the right Pokemon name"
                        number=6
                        context={"name":name,"details":details,"number":number}
                        return render(request,"trial.html",context)
                    else:
                        print("ff")
                        for result in r['results']:
                            if result['name']==pk:
                                for names in requests.get(result['url']).json()['pokemon']:
                                    name.append(names['pokemon']['name'])
                                    if request.POST['pokemon']==names['pokemon']['name']:
                                        url=requests.get(names['pokemon']['url']).json()['sprites']['front_default']
                                        print(url)
                                        number=url.split("/")[-1].split(".")[0]
                                        print(url.split("/")[-1].split(".")[0])
                                        details=request.POST['pokemon']
                                        context={"name":name,"details":details,"number":number}
                                        return render(request,"trial.html",context)
    else:
        context={"name":name,"details":"","number":6}
        return render(request,"trial.html",context)

def url(request,number):
    return redirect("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+str(number)+".png")


# 4 TH TASK

def displaypokemon(request):
    if request.method=="POST":
        types=[]
        names=[]
        move=[]
        abilities=[]
        type=(request.POST['PokemonType'])
        name=(request.POST['Pokemon'])
        u_name=name+type
        for result in r['results']:
            #print(result['name'])
            types.append(result['name'])
            
            if result['name']==request.POST['PokemonType']:
                for data in requests.get(result['url']).json()['pokemon']:
                    #print(data['pokemon']['name'])
                    names.append(data['pokemon']['name'])    
                    if data['pokemon']['name']==request.POST['Pokemon']:
                        #print(requests.get(data['pokemon']['url']).json().keys())
                        for ability in requests.get(data['pokemon']['url']).json()['abilities']:
                            abilities.append(ability['ability']['name'])
                        height=( requests.get(data['pokemon']['url']).json()['height'])
                        weight=( requests.get(data['pokemon']['url']).json()['weight'])
                        for moves in requests.get(data['pokemon']['url']).json()['moves']:
                            move.append(moves['move']['name'])
                            #print(move)
                        url=(requests.get(data['pokemon']['url']).json()['sprites']['front_default'])
                        pokemondata=PokemonData(name=name, type=type,height=height,weight=weight,move=move,image=url,abilities=abilities,u_name=u_name)
                        isexists=pokemondata.isExists()
                        if isexists==True:
                            error="You are entering same pokemon of same type."
                        else:
                            pokemondata.save()
                            error=""
        pokemon_data=PokemonData.objects.all()
        context={"name":name,"type":type,"height":height,"weight":weight,"move":move,"abilities":abilities,"url":url,"data":pokemon_data,"error":error}
        return render(request,"pokemondetails.html",context)            
    else:
        context={"name":"","type":"","height":"","weight":"","move":"","abilities":"","url":"","data":"","error":"","error_mssage":""}
        return render(request,"pokemondetails.html",context)

def displaypokemon2(request):
    if request.method=="POST":
        types=[]
        names=[]
        move=[]
        abilities=[]
        type=(request.POST['PokemonType'])
        name=(request.POST['Pokemon'])
        u_name=name+type
        for result in r['results']:
            #print(result['name'])
            types.append(result['name'])
            if type not in types:
                print("wrong type")
                error_message="You have entered wrong type"
                error_name_message=""
                context={"name":"","type":"","height":"","weight":"","move":"","abilities":"","url":"","data":"","error":"","error_message":error_message,"error_name_message":error_name_message}
            else:
                error_message=""
                if result['name']==request.POST['PokemonType']:
                    for data in requests.get(result['url']).json()['pokemon']:
                        #print(data['pokemon']['name'])
                        names.append(data['pokemon']['name'])
                        if name not in names:
                            error_message=""
                            error_name_message="You have entered wrong name of pokemon"
                            context={"name":"","type":"","height":"","weight":"","move":"","abilities":"","url":"","data":"","error":"","error_message":error_message,"error_name_message":error_name_message}
                        else:
                            error_message=""
                            error_name_message=""    
                            if data['pokemon']['name']==request.POST['Pokemon']:
                                #print(requests.get(data['pokemon']['url']).json().keys())
                                for ability in requests.get(data['pokemon']['url']).json()['abilities']:
                                    abilities.append(ability['ability']['name'])
                                height=( requests.get(data['pokemon']['url']).json()['height'])
                                weight=( requests.get(data['pokemon']['url']).json()['weight'])
                                for moves in requests.get(data['pokemon']['url']).json()['moves']:
                                    move.append(moves['move']['name'])
                                    #print(move)
                                url=(requests.get(data['pokemon']['url']).json()['sprites']['front_default'])
                                pokemondata=PokemonData(name=name, type=type,height=height,weight=weight,move=move,abilities=abilities,u_name=u_name,header_image=url)
                                isexists=pokemondata.isExists()
                                if isexists==True:
                                    error="You are entering same pokemon of same type."
                                else:
                                    pokemondata.save()
                                    error=""
                                pokemon_data=PokemonData.objects.all()
                                context={"name":name,"type":type,"height":height,"weight":weight,"move":move,"abilities":abilities,"url":url,"data":pokemon_data,"error":error,"error_message":error_message,"error_name_message":error_name_message}
        
        return render(request,"pokemondetails.html",context)            
    else:
        error_name_message=''
        error_message=''
        context={"name":"","type":"","height":"","weight":"","move":"","abilities":"","url":"","data":"","error":"","error_message":error_message,"error_name_message":error_name_message}
        return render(request,"pokemondetails.html",context)

                            
