from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
driver=webdriver.Chrome("C:\\Users\\Admin\\Desktop\\Python Selenium\\chromedriver.exe")
driver.maximize_window()
url='https://www.cleartrip.com/'
driver.get(url)
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='px-1 plNew  flex flex-middle nmx-1 pb-1']").click()
import selenium.webdriver.support.expected_conditions as EC
# driver.find_element(By.CLASS_NAME, "mt-3 mr-3 r-0 p-absolute c-pointer").click()
# alert=Alert(driver)
# driver.switch_to.alert
# alert.dismiss()
