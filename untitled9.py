import requests
import json


key = '06255308bac1169f4742fb7e2daad757'
url = 'https://api.themoviedb.org/3/movie/11?api_key=06255308bac1169f4742fb7e2daad757'
response = requests.get(url)
data = response.json()
print(data)


movies = []


movies.append(data)
with open ('movie.json','w') as file:
    json.dump(movies,file,indent=3)
with open('movie.json','r') as file:
    json_object = json.load(file)

print(json_object)