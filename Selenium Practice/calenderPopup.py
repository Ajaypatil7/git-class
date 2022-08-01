from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\\Users\\Admin\\Desktop\\Python Selenium\\chromedriver.exe")

#To get the Dates remaining in the current month
driver.get('https://www.yatra.com/')
driver.maximize_window()
time.sleep(3)
# driver.find_element(By.CLASS_NAME, "BE_flight_origin_date").click()
# time.sleep(5)
#
# dates=driver.find_elements(By.XPATH, '''//div[text()="July' 22"]/../..//div[@id='month-scroll0']//td[not(@class='inActiveTD weekend' or @class='inActiveTD')]''')
#
# for date in dates:
#     print(date.text)
# time.sleep(5)



# Select a date in the month
date_from_user=input("Enter date to be selected in dd-mm-yyyy format")
driver.find_element(By.CLASS_NAME, "BE_flight_origin_date").click()
time.sleep(3)







driver.close()







