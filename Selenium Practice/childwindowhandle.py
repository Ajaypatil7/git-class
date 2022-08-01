import webbrowser
import keyboard
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("C:\\Users\\Admin\\Desktop\\Python Selenium\\chromedriver.exe")
driver.maximize_window()
url='http://demowebshop.tricentis.com/'
driver.get(url)
time.sleep(3)
print("Current window handle is:", driver.current_window_handle)
elements=driver.find_elements(By.XPATH,"//ul[@class='top-menu']/li")
act=ActionChains(driver)


time.sleep(5)







driver.close()