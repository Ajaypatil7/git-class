from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver= webdriver.Chrome('C:\\Users\\Admin\\Desktop\\Python Selenium\\chromedriver.exe')

driver.get("http://demowebshop.tricentis.com/")

wait=WebDriverWait(driver,20)
wait.until()
ec.alert_is_present()