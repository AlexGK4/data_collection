import requests


user = input('Введите имя пользователя: ')
main_link = f'https://api.github.com/users/{user}/repos?'
response = requests.get(main_link)

repos_list = []
for repo in response.json():
    repos_list.append(repo['full_name'])

repos_list = str(repos_list)
print(repos_list)
with open('HW1.json', 'w') as f:
    f.write(repos_list)
