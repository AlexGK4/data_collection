#mail.ru

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()
chrome_options.add_argument('start-maximized')

driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.get('https://mail.ru/')

login = driver.find_element_by_id('mailbox:login-input')
login.send_keys('study.ai_172')
login.send_keys(Keys.ENTER)

time.sleep(2)

password = driver.find_element_by_id('mailbox:password-input')
password.send_keys('NextPassword172')
password.send_keys(Keys.ENTER)

time.sleep(5)

while True:
    time.sleep(3)
    elements = driver.find_elements_by_xpath("//div[@class='dataset__items']/a")
    action = ActionChains(driver)
    action.move_to_element(elements[-1])
    action.perform()

letters_block = driver.find_elements_by_xpath("//div[@class='dataset__items']/a")
letters = []
for letter in letters_block:
    letter_data = {}
    letter_data['sender'] = letter.find_element_by_class_name('ll-crpt').text
    letter_data['date'] = letter.find_element_by_xpath("//div[@class='llc__item llc__item_date']").text
    letter_data['theme'] = letter.find_element_by_class_name('ll-sj__normal').text
    letter_data['link'] = letter.get_attribute('href')
    letters.append(letter_data)
print(letters)

driver.close()
