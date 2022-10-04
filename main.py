import time, requests, yadisk
from pprint import pprint

#токен для вк = https://oauth.vk.com/authorize?client_id=51437262&scope=photos&response_type=token

y = yadisk.YaDisk(token="y0_AgAAAABk33T_AADLWwAAAADP0R4mdGLnpH3gR0a8dvtGvAxmfqPDS0Q")
access_token = 'vk1.a.xziybuvUwE9kY074NHeAKRubzRwjMNwQ3YAbA-Yk60ifc1UDxtqyIRKKh_ZmuVipwGkn-kvgjzYvvC7hx5NX3N-thw9tqb9bjq5d6bC5oezm7p2WNj9YN7iR4IIHXTeq8Mqd2YFKOrHwaWXanRWP-hxt8god5T-NW38f0-zRBYGeIlZ5ahbQoxU2Xc2vTbU5'
user_id = 217566226

url = 'https://api.vk.com/method/photos.getAll'
params = {
    'owner_id': user_id,
    'extended': 1,
    'photo_sizes': 1,
    'access_token': access_token,
    'count': 2,
    'v': 5.131
}

res = requests.get(url, params=params).json()
res = res['response']['items']
sizes_photos = {}
last_photos = {}

for i in res:
    likes = i['likes']
    sizes = i['sizes']
    for i in sizes:
        aa = i['url']
        size = aa.rpartition('size=')[-1]
        size = size.rpartition('&quality=')[0]
        size1 = size.split('x')
        summ = int(size1[0]) + int(size1[1])
        sizes_photos[summ] = [i['url']]
    peremen1 = sorted(sizes_photos.keys())[-1]
    peremen2 = sizes_photos[peremen1]
    last_photos[peremen2[0]] = str(likes['count'])
    sizes_photos.clear()

pprint(last_photos)

for key, value in last_photos.items():
    #y.ppppp(key, f'{value}.jpeg')
    pass




