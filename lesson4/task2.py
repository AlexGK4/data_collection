#yndex.news

from pprint import pprint
from lxml import html
import requests
import datetime

user_agent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
main_link = 'https://yandex.ru/news'

response = requests.get(f'{main_link}', headers=user_agent)
dom = html.fromstring(response.text)

main_news = dom.xpath("//body/div[@id='neo-page']/div[@class='neo-app news-app']/div[@class='news-app__content']/div[@class='mg-grid__row mg-grid__row_gap_8']/div[@class='mg-grid__col mg-grid__col_xs_12 mg-grid__col_sm_9']/div[3]/div[@class='mg-grid__col mg-grid__col_xs_4']/article[@class='mg-card news-card news-card_single news-card_type_image mg-grid__item mg-grid__item_type_card']")
list_news = []
for item in main_news:
    some_news = {}
    name = item.xpath('.//a/h2/text()')
    source = item.xpath('.//a/text()')
    link = item.xpath('.//div[@class="mg-card-source news-card__source"]//a/@href')
    date = item.xpath(".//div[@class='mg-card-footer news-card__footer news-card__footer_type_image']//span[@class='mg-card-source__time']/text()")

    if str(date[0]).startswith('вчера'):
        datetime_news = 'вчера'
    else:
        datetime_news = datetime.datetime.today().strftime('%Y-%m-%d')
    datetime_news = datetime_news +' ' + str(date[0])
    some_news['name'] = name
    some_news['source'] = source
    some_news['link'] = link
    some_news['datetime'] = datetime_news
    list_news.append(some_news)

news_block = dom.xpath("//div[@id='neo-page']/div[@class='neo-app news-app']/div[@class='news-app__content']/div[@class='mg-grid__row mg-grid__row_gap_8']/div[@class='mg-grid__col mg-grid__col_xs_12 mg-grid__col_sm_9']/div[3]/div[@class='mg-grid__col mg-grid__col_xs_8']//div[@class='mg-grid__col mg-grid__col_xs_6']")

for item in news_block:
    some_news = {}
    name = item.xpath('.//a/h2/text()')
    source = item.xpath('.//a/text()')
    link = item.xpath('.//div[@class="mg-card-source news-card__source"]//a/@href')
    date = item.xpath(
        ".//div[@class='mg-card-footer news-card__footer news-card__footer_type_image']//span[@class='mg-card-source__time']/text()")
    if str(date[0]).startswith('вчера'):
        datetime_news = str(date[0])
    else:
        datetime_news = datetime.datetime.today().strftime('%Y-%m-%d')
        datetime_news = datetime_news + ' ' + str(date[0])
    some_news['name'] = name
    some_news['source'] = source
    some_news['link'] = link
    some_news['datetime'] = datetime_news
    list_news.append(some_news)

pprint(list_news)