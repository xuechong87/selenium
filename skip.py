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
	conda = 1
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

	#跳过
	@unittest.skip(u'跳过')
	def testOther(self): 
		print('ski1')
		pass

	#跳过
	@unittest.skipIf(conda==1,u'跳过')
	def testSkipA(self): 
		print('ski2')
		pass


	@unittest.skipUnless(conda==0, u"除数为0")
	def testSkipB(self):
		print(conda)

	@unittest.expectedFailure
	def testFail(self):
		self.assertTrue(conda != conda)

	#after test 释放资源写在此处
	def tearDown(self):
		self.driver.quit()
		pass
	pass


#程序入口
if __name__ == '__main__':
	unittest.main()