#superjob

from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

# search_request = input('Введите профессию: ')
user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
search_request = 'повар'


def find_salary():
    try:

        step1 = vacancy.find('span', {'class': '_3mfro _2Wp8I PlM3e _2JVkc _2VHxz'}).text
        # print(step1)
        if step1.startswith('от'):
            step1 = step1.replace('\xa0', ' ')
            split_var1 = step1.split(' ')
            min_salary = int(split_var1[1] + split_var1[2])
            max_salary = None
            currency = split_var1[3]

        elif step1.startswith('до'):
            step1 = step1.replace('\xa0', ' ')
            split_var1 = step1.split(' ')
            min_salary = None
            max_salary = int(split_var1[1] + split_var1[2])
            currency = split_var1[3]

        elif step1 == 'По договоренности':
            min_salary = None
            max_salary = None
            currency = None

        else:
            step1 = step1.replace('\xa0', ' ')
            split_var1 = step1.split('—')
            split_var2 = split_var1[0].split(' ')
            split_var3 = split_var1[1].split(' ')
            min_salary = int(split_var2[0] + split_var2[1])
            max_salary = int(split_var3[1] + split_var3[2])
            currency = split_var3[3]

    except:
        min_salary = None
        max_salary = None
        currency = None
    return min_salary, max_salary, currency

pager = 1

while True:
    main_link = 'https://www.superjob.ru'


    sj_params = {'keywords': search_request,
                 'geo[t][0]': 4,
                 'page': pager
                 }

    html = requests.get(main_link + '/vacancy/search/', params=sj_params, headers=user_agent)
    dom = bs(html.text, 'html.parser')
    vac_list = dom.find_all('div', {'class': 'iJCa5 f-test-vacancy-item _1fma_ undefined _2nteL'})
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
    # pprint(vacancies)

    if dom.find('span', {'class': '_3IDf-'}):
        pager += 1

    else:
        break
print(1)

