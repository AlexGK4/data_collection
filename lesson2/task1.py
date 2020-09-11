#сайт HH.ru

from bs4 import BeautifulSoup as bs
import requests
import pprint

def count_pages(): #функция для определения количества страниц
    pager_tag = dom.find('div', {'data-qa': 'pager-block'})
    if pager_tag != None:
        find_child = pager_tag.find('span', {'class': 'pager-item-not-in-short-range'}, recursive=False)
        pages = int(find_child.find('a').getText()) - 1
    else:
        pages = 0
    return pages


user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
# search_request = input('Введите профессию: ')
search_request = 'повар'
main_link = 'https://hh.ru/'
pager = 0
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
vac_list = vacancy_block.find_all('div', {'class': 'vacancy-serp-item'})




def find_salary(): #функция для нахождения зарплаты
    try:

        step1 = vacancy.find('div', {'class': 'vacancy-serp-item__sidebar'})
        step2 = step1.find('span').text
        if step2 != 'по договоренности':
            split_var1 = step2.split(' ')
            split_var2 = split_var1[0].split('\xa0')
            min_salary = int(split_var2[0]) * 1000
            split_var3 = split_var2[1].split('-')
            max_salary = int(split_var3[1]) * 1000
            currency = split_var1[1]

        elif step2.startswitch('от'):
            split_var1 = step2.split(' ')
            split_var2 = split_var1[0].split('\xa0')
            min_salary = int(split_var2[0]) * 1000
            max_salary= None
            currency = split_var1[1]

        else:
            min_salary = ''
            max_salary = ''
            currency = ''

    except:
        min_salary = 'q'
        max_salary = 'q'
        currency = 'q'
    return min_salary, max_salary, currency


vacancies = []

for vacancy in vac_list:
    min_salary, max_salary, currency = find_salary()
    vacancy_data = {}
    vacancy_data['name'] = vacancy.find('a').getText()
    vacancy_data['link'] = vacancy.find('a')['href']
    vacancy_data['site'] = main_link
    vacancy_data['min_salary'] = min_salary
    vacancy_data['max_salary'] = max_salary
    vacancy_data['currency'] = currency
    vacancies.append(vacancy_data)

print()
















paging = []
if count_pages() != 0:
    while pager != count_pages():
        vacancy_block = dom.find('div', {'class': 'vacancy-serp'})
        vacancies_list = vacancy_block.find_all('div', {'class': 'vacancy-serp-item'})
        paging.append(vacancies_list)
        pager += 1
    else:
        vacancy_block = dom.find('div', {'class': 'vacancy-serp'})
        vacancies_list = vacancy_block.find_all('div', {'class': 'vacancy-serp-item'})



def find_max_salary():   #функция для нахождения максимальной зарплаты
    for vac_list in paging:
        for vacancy in vac_list:
            var1 = vacancy.find('div', {'class': 'vacancy-serp'})

        if var1 != None:
            var2 = var1.find('div', {'class': 'vacancy-serp-item__sidebar'})
            var3 = var2.find('span').text
            split_var1 = var3.split(' ')
            split_var2 = split_var1[0].split('\xa0')
            split_var3 = split_var2[1].split('-')
            max_salary = int(split_var3[1]) * 1000
        else:
            max_salary = None
    return (max_salary)


def find_currency():  #функция для определения валюты
    for vacancy in vacancies_list:
        var1 = vacancy.find('div', {'class': 'vacancy-serp'})
        if var1 != None:
            var2 = var1.find('div', {'class': 'vacancy-serp-item__sidebar'})
            var3 = var2.find('span').text
            split_var3 = var3.split(' ')
            currency = split_var3[1]
        else:
            currency = None
    return currency

