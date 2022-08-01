from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#chrm="C:\\Users\\Admin\\Desktop\\Python Selenium\\chromedriver.exe"
#driver= webdriver.Chrome(executable_path=chrm)
gck="C:\\Users\\Admin\\Desktop\\Python Selenium\\geckodriver.exe"
driver=webdriver.Firefox(executable_path=gck)
driver.get("https://www.facebook.com/")
driver.get("https://www.instagram.com/")
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.close()
