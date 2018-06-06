# selenium
======

## python环境与selenium安装


* 下载python

	windows中下载msi安装包即可

	[https://www.python.org/](https://www.python.org/)


* 安装selenium
	
	在windows powershell中执行命令
	
	*pip install -U selenium*


	在Python 2 >=2.7.9 或 Python 3 >=3.4 版本以上pip工具会集成在安装包中 
	如果你当前python版本低于以上版本 请先升级


* 安装ChromeDriver

	[ChromeDriver项目地址](https://sites.google.com/a/chromium.org/chromedriver/home) (需要科学上网)

	将下载后的文件放入chrome安装目录下 
	例如 : *C:\Program Files (x86)\Google\Chrome\Application*


	mac/linux放在/usr/bin目录下


	*chromedriver版本与chrome版本应互相对应 
	可以查看[此处](https://sites.google.com/a/chromium.org/chromedriver/downloads)(需要科学上网)找到与自己当前chrome版本相对的版本*



## hello world
	
```python

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

```

## 单元测试

```python
	# coding:utf-8
	import time
	import unittest
	
	from selenium import webdriver
	
	
	class IndexAlive(unittest.TestCase):
	
		#准备工作写在此处
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
	
	#程序入口
	if __name__ == '__main__':
		unittest.main()


```