from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time, keyboard
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome('C:\\Users\\Admin\\Desktop\\Python Selenium\\chromedriver.exe')
driver.get("http://demowebshop.tricentis.com/")

driver.maximize_window()

a=ActionChains(driver)
computers= driver.find_element(By.LINK_TEXT, "Computers")
# a.context_click(computers).perform()
# keyboard.press('t')
# time.sleep(5)
a.drag_and_drop(computers,driver.find_element(By.ID, "small-searchterms") )

time.sleep(5)


print("Done")
driver.close()