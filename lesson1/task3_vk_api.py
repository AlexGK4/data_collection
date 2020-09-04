import requests
from pprint import pprint

# vk_login = input('Введите ваш логин для сайта vk.com/: ')
# vk_pass = input('Введите ваш пароль для сайта vk.com/: ')
#
auth = f'https://oauth.vk.com/authorize'
auth_params = {'client_id': '7586643',
               'redirect_uri': 'https://oauth.vk.com/blank.html',
               'scope': 'friends',
               'response_type': 'token',
               'v': 5.52
               }

response_auth = requests.get(auth, params=auth_params)

main_link = f'https://api.vk.com/method/friends.getOnline'
friends_param = {'user_id': '2669006',
                 'access_token': ...,
                 'v': 5.52
                 }

friends_online = requests.get(main_link, params=friends_param)
