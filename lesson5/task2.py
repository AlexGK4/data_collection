#М-видео

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome('./chromedriver', options=chrome_options)

driver.get('https://www.mvideo.ru/')
pages = 0
pages_left = 0
hits = []

while True:
    try:
        goods = driver.find_elements_by_xpath(
            "//div[@class='wrapper']/div[@class='page-content']/div[@class='main-holder']/div[5]/div[@class='gallery-layout gallery-layout_products gallery-layout_product-set grid-view']/div[@class='gallery-content accessories-new ']/div[@class='accessories-carousel-holder carousel tabletSwipe']//li")

        for good in goods:
            good_data = {}
            good_data['name'] = good.find_element_by_class_name('sel-product-tile-title').text
            hits.append(good_data)

        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='wrapper']/div[@class='page-content']/div[@class='main-holder']/div[5]/div[@class='gallery-layout gallery-layout_products gallery-layout_product-set grid-view']//a[@class='next-btn c-btn c-btn_scroll-horizontal c-btn_icon i-icon-fl-arrow-right']"))
        )
        time.sleep(2)
        button.click()
        pages += 1
    except:
        print('Это все хиты продаж!')
        break

final_hits = []
for i in hits:
    if i not in final_hits and i != '':
        final_hits.append(i)

print(final_hits)
