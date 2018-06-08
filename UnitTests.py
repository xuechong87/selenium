# coding:utf-8
import time
import unittest
# from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class IndexAlive(unittest.TestCase):

	#准备工作写在此处
	#setUp 方法是初始化的一部分, 该方法会在该测试类中的每一个测试方法被执行前都执行一遍
	def setUp(self):
		self.driver = webdriver.Chrome()
		pass

	def testIndexAlive(self): #测试方法必须以test开头
		driver = self.driver
		driver.get('https://www.eastlending.com/')

		titleEle = driver.find_element_by_tag_name('title')
		titleStr = titleEle.parent.title

		print('title is :' + titleStr)
		assert u"东方汇" in driver.title #通过断言判断功能是否按预期进行
		pass

	#after test 释放资源写在此处
	def tearDown(self):
		self.driver.quit()
		pass
	pass


class Login(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		pass

	def testLogin(self):
		driver = self.driver

		driver.get('http://dfjktest.eastlending.cn/portal/login')

		#输入用户名密码
		usrEle = driver.find_element_by_name('username')
		usrEle.send_keys('admin')

		pwdEle = driver.find_element_by_name('password')
		pwdEle.send_keys('ddddd')

		#点击提交
		loginBtn = driver.find_element_by_id('login-btn')
		loginBtn.click()

		try:
			#根据title 判断登录是否成功
			element = WebDriverWait(driver,1).until(EC.title_contains("Management"))
			print("login suc")
			pass
		except Exception, e:
			print('login failed')
			print(e.message.decode('utf-8'))
			print(type(e.message))

		assert u"Management" in driver.title

		pass


	@unittest.expectedFailure
	def testLoginFail(self):
		driver = self.driver

		driver.get('http://dfjktest.eastlending.cn/portal/login')

		#输入用户名密码
		usrEle = driver.find_element_by_name('username')
		usrEle.send_keys('admin')

		pwdEle = driver.find_element_by_name('password')
		pwdEle.send_keys('asdasd')

		#点击提交
		loginBtn = driver.find_element_by_id('login-btn')
		loginBtn.click()
		pass


	def tearDown(self):
		self.driver.quit()
		pass
	pass

#程序入口
if __name__ == '__main__':
	unittest.main()