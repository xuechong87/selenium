#coding:utf-8

import time
from selenium import webdriver #导入需要的包

#初始化浏览器
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')  # 写地址
driver.get('https://www.eastlending.com/') #打开一个网址

#寻找base标签 并打印其中的href
baseEle = driver.find_element_by_tag_name('base')
print('base href is :' + baseEle.get_attribute('href')) 

#打印title中的内容
titleEle = driver.find_element_by_tag_name('title')
titleStr = titleEle.parent.title

print('title is :' + titleStr)

# time.sleep(1)
driver.quit() #关闭浏览器

print('press any key')
input()