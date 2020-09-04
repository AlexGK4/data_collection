import requests


main_link = f'https://www.flickr.com/services/api/explore/flickr.auth.oauth.checkToken'

flickr_params = {"api_key": '7967ae95af91ee3ba48a0dc5f342463e',
                 'auth_token': 'ec16657d7c68d556'
                 }
response = requests.get(main_link, params=flickr_params)
print(response.text)

with open('HW2.json', 'w') as f:
    f.write(response.text)
