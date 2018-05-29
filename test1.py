#coding:utf-8

import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')  # 写地址
driver.get('https://www.eastlending.com/')
baseEle = driver.find_element_by_tag_name('base')

print('base href is :' + baseEle.get_attribute('href'))

titleEle = driver.find_element_by_tag_name('title')
titleStr = titleEle.parent.title

print('title is :' + titleStr)

# time.sleep(1)
driver.quit()
print('press any key')
input()