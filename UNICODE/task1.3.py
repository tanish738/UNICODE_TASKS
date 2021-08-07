import requests
import pandas

import json
data=[]
poke_keys=[]

r=requests.get("https://pokeapi.co/api/v2/type/").json()
#print(r['results'])
for result in r['results']:
    #print(result['name'])
    if result['name']=="water":
        
            for data in requests.get(result['url']).json()['pokemon']:
                #print(data['pokemon']['name'])
                if data['pokemon']['name']=="blastoise":
                    '''print(requests.get(data['pokemon']['url']).json().keys())
                    for ability in requests.get(data['pokemon']['url']).json()['abilities']:
                        print(ability['ability']['name'])
                    print( requests.get(data['pokemon']['url']).json()['height'])
                    print( requests.get(data['pokemon']['url']).json()['weight'])
                    for moves in requests.get(data['pokemon']['url']).json()['moves']:
                        print(moves['move']['name'])'''
                    url=requests.get(data['pokemon']['url']).json()['sprites']['front_default']
                        
                        
#print(url.split("/")[-1].split(".")[0])
        

