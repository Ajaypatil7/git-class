from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome('C:\\Users\\Admin\\Desktop\\Python Selenium\\chromedriver.exe')
driver.maximize_window()
#driver.get('file:///C:/Users/Admin/Desktop/Python%20Selenium/practice%20docs/demo-html/demo.html')


#s1=Select(driver.find_element(By.ID, "standard_cars"))
#To check it is multi select or single select
# if s1.is_multiple:
#     print('It is multiselect class')
# else:
#     print('It is single select class')

#Count the no of options
# cnt= [option for option in s1.options]
# print(len(cnt))

#print all options in the list box.
# opt= [option for option in s1.options]
# for i in opt:
#     print(i.text)

#select all the options from the select class.
      #If it is a single select then it will select the last option and doesn't throw an error.
      #if It is multiselect then it will select all the options.
# option=s1.options
# for i in option:
#     s1.select_by_visible_text(i.text)

#Write a program to get all the option from the drop down, sort all the option and print
# opt=[option.text for option in s1.options]
# opt.sort()
# print(opt)



# s1.select_by_visible_text('Ford')
# time.sleep(2)
# s1.select_by_index(4)
# time.sleep(3)
# driver.close()




#Example1
driver.get('https://www.yatra.com/')
time.sleep(5)
driver.find_element(By.NAME, "flight_origin").click()
time.sleep(5)
sources=driver.find_elements(By.XPATH, '//div[@class="ac_results origin_ac"]//p[@class="ac_cityname"]')
print('Done')
for s in sources:
    print(s.text)
print(sources)