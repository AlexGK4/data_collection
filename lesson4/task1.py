#lenta.ru

from pprint import pprint
from lxml import html
import requests

user_agent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
main_link = 'https://lenta.ru'

response = requests.get(f'{main_link}', headers=user_agent)
dom = html.fromstring(response.text)

first_news = dom.xpath('//div[@class="first-item"]//h2//a')

news_list = []
source = 'lenta.ru'
for item in first_news:
    some_news = {}
    name = item.xpath('./text()')
    link = item.xpath('./@href')
    datetime = item.xpath('./time/@datetime')
    some_news['name'] = name
    some_news['source'] = source
    some_news['link'] = link
    some_news['datetime'] = datetime
    news_list.append(some_news)

news_block = dom.xpath('//section[@class="row b-top7-for-main js-top-seven"]//div[@class="item"]//a')
for item in news_block:
    some_news = {}
    name = item.xpath('./text()')
    name = name[0].replace('\xa0', ' ')
    link = item.xpath('./@href')
    datetime = item.xpath('./time/@datetime')
    some_news['name'] = name
    some_news['source'] = source
    some_news['link'] = link
    some_news['datetime'] = datetime
    news_list.append(some_news)
pprint(news_list)