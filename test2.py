#coding:utf-8

import time
from selenium import webdriver #导入需要的包

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#初始化浏览器
driver = webdriver.Chrome()  
driver.get('http://dfjktest.eastlending.cn/portal/login')


#输入用户名密码
usrEle = driver.find_element_by_name('username')
usrEle.send_keys('admin')

pwdEle = driver.find_element_by_name('password')
pwdEle.send_keys('asdasd')

点击提交
loginBtn = driver.find_element_by_id('login-btn')
loginBtn.click()


try:
	element = WebDriverWait(driver,1).until(EC.title_contains("Management"))
    
	print("login suc")
	pass
except Exception, e:
	print('login failed')
	print(e.message.decode('utf-8'))
	print(type(e.message))

raw_input('enter any key to quit')
driver.quit()