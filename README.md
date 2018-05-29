# selenium

selenium 学习

## python环境与selenium安装


* 下载python

	[https://www.python.org/](https://www.python.org/)


* 安装selenium
	
	*pip install -U selenium*


	在Python 2 >=2.7.9 或 Python 3 >=3.4 版本以上pip工具会集成在安装包中 
	如果你当前pyton版本低于以上版本 请先升级

* 安装ChromeDriver

	[ChromeDriver项目地址](https://sites.google.com/a/chromium.org/chromedriver/home) (需要科学上网)

	将下载后的文件放入chrome安装目录下 
	例如 :C:\Program Files (x86)\Google\Chrome\Application

## hello world
	
```pytthon

	import time
	from selenium import webdriver

	driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')  
	driver.get('https://www.eastlending.com/')
	titleEle = driver.find_element_by_tag_name('base')

	print(titleEle.get_attribute('href'))
	time.sleep(5)
	driver.quit()
	print('press any key')
	input()
```
