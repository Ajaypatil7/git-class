from selenium import webdriver
import time
from selenium.webdriver.common.by  import By
driver= webdriver.Chrome('C:\\Users\\Admin\\Desktop\\Python Selenium\\chromedriver.exe')
url='http://demowebshop.tricentis.com/'
driver.get(url)
driver.maximize_window()
time.sleep(4)

driver.find_element(By.CLASS_NAME, 'ico-register').click()
time.sleep(1)

# driver.find_element(By.ID, 'gender-male').click()
# driver.find_element(By.ID, 'FirstName').send_keys('ABCD')
# driver.find_element(By.ID, 'LastName').send_keys('PQRS')
# driver.find_element(By.ID, 'Email').send_keys('abcd@gmail.com')
nav_elements= driver.find_elements(By.XPATH, '//ul[@class="top-menu"]/li')
for item in nav_elements:
    print(item.text)
    item.text
time.sleep(2)


driver.close()
print('done')