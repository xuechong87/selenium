
import time
from selenium import webdriver

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.eastlending.com/')
titleEle = driver.find_element_by_tag_name('base')

print(titleEle.get_attribute('href'))
time.sleep(5)
driver.quit()
print('press any key')
input()