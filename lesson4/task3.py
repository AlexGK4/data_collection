#news.mail.ru

from pprint import pprint
from lxml import html
import requests

user_agent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
main_link = 'https://news.mail.ru/'

response = requests.get(f'{main_link}', headers=user_agent)
dom = html.fromstring(response.text)

main_news = dom.xpath("//div[@class='layout']/div[contains(@class,'js-module')]/div[@class='block block_separated_top rb_nat']/div[@name='clb20268392']/div[@class='cols cols_margin cols_percent']/div[@class='cols__wrapper']/div[1]")
list_news = []

def find_source(link):
    resp = requests.get(f'{link}', headers=user_agent)
    d = html.fromstring(resp.text)
    source = d.xpath("//a[@class='link color_gray breadcrumbs__link']//span[@class='link__text']/text()")
    return source

def find_time(link):
    resp = requests.get(f'{link}', headers=user_agent)
    d = html.fromstring(resp.text)
    datetime = d.xpath("//span[@class='note__text breadcrumbs__text js-ago']/@datetime")
    return datetime

for item in main_news:
    some_news = {}
    name = item.xpath('.//span[@class="newsitem__title-inner"]/text()')
    link = item.xpath('.//a[@class="newsitem__title link-holder"]/@href')
    link_for_def = str(link[0])
    source = find_source(link_for_def)
    time = find_time(link_for_def)
    some_news['name'] = name
    some_news['link'] = link
    some_news['source'] = source
    some_news['time'] = time
    list_news.append(some_news)

news_block = dom.xpath("//div[@class='block block_separated_top rb_nat']//div[@class='cols__wrapper']//div[@class='cols__column cols__column_small_percent-50 cols__column_medium_percent-50 cols__column_large_percent-50 link-hdr'][1]//ul/li")

for item in news_block:
    some_news = {}
    name = item.xpath('./span/a/span/text()')
    link = item.xpath('./span/a/@href')
    link_for_def = str(link[0])
    source = find_source(link_for_def)
    time = find_time(link_for_def)
    some_news['name'] = name
    some_news['link'] = link
    some_news['source'] = source
    some_news['time'] = time
    list_news.append(some_news)
pprint(list_news)