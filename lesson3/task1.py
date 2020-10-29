# HH.ru


from bs4 import BeautifulSoup as bs
import requests
from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost',  27017)
db = client['hh_database']
vac_data = db.vac_data


user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
search_request = input('Введите профессию: ')
# search_request = 'повар'

def find_salary(): #функция для нахождения зарплаты
    try:

        step1 = vacancy.find('div', {'class': 'vacancy-serp-item__sidebar'})
        step2 = step1.find('span').text

        if step2.startswith('от'):
            step2 = step2.replace('\xa0', ' ')
            split_var1 = step2.split(' ')
            min_salary = int(split_var1[1] + split_var1[2])
            max_salary = None
            currency = split_var1[3]

        elif step2.startswith('до'):
            step2 = step2.replace('\xa0', ' ')
            split_var1 = step2.split(' ')
            min_salary = None
            max_salary = int(split_var1[1] + split_var1[2])
            currency = split_var1[3]

        elif step2 == 'По договоренности':
            min_salary = None
            max_salary = None
            currency = None

        else:
            step3 = step2.replace('\xa0', ' ')
            split_var1 = step3.split(' ')
            split_var2 = split_var1[1].split('-')
            min_salary = int(split_var1[0]+split_var2[0])
            max_salary = int(split_var2[1]+split_var1[2])
            currency = split_var1[3]

    except:
        min_salary = None
        max_salary = None
        currency = None
    return min_salary, max_salary, currency



pager = 0

while True:
    main_link = 'https://hh.ru/'

    hh_params = {'text': search_request,
                 'L_save_area': 'true',
                 'clusters': 'true',
                 'enable_snippets': 'true',
                 'search_field': 'name',
                 'showClusters': 'true',
                 'page': pager,
                 'from': 'cluster_area',
                 'area': 1
                 }

    html = requests.get(main_link + 'search/vacancy', params=hh_params, headers=user_agent)
    dom = bs(html.text, 'html.parser')

    vacancy_block = dom.find('div', {'class': 'vacancy-serp'})
    vacancy_list = vacancy_block.find_all('div', {'class': 'vacancy-serp-item'})

    vacancies = []

    for vacancy in vacancy_list:
        min_salary, max_salary, currency = find_salary()
        vacancy_data = {}
        vacancy_data['name'] = vacancy.find('a').getText()
        vacancy_data['link'] = vacancy.find('a')['href']
        vacancy_data['site'] = main_link
        vacancy_data['min_salary'] = min_salary
        vacancy_data['max_salary'] = max_salary
        vacancy_data['currency'] = currency
        vacancies.append(vacancy_data)
        pprint(vacancies)

    if dom.find('a', {'data-qa': 'pager-next'}):
        pager += 1

    else:
        break

def add_vac(vac_list):
    vac_data.insert_many(vac_list)

def show_salary():
    salary = int(input('Введите желаемую зарплату: '))
    for data in vac_data.find({'$or': [{'min_salary': {'$gte': salary}}, {'max_salary': {'$gte': salary}}]}):
        pprint(f'По вашему запросу подходит {data}')

def nev_vacs(vac_list):
    for vacs in vac_list:
        for link in vacs.get('link'):
            if vac_data.find({'link': link}):
                print('Вакансия уже в базе')
            else:
                vac_data.insert_one(vacs)

# add_vac(vacancies)

