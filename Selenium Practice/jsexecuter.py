from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome('C:\\Users\\Admin\\Desktop\\Python Selenium\\chromedriver.exe')
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()

#Write a script to create the alert pop up?
# driver.execute_script("alert('Welcome to Pyspiders')")    # It is used to throw the alert
# time.sleep(10)


#Write a script to get the domain name?
# domain_name=driver.execute_script("return document.domain" )
# print(domain_name)

#Write a script to get the domain name?
# domain_title=driver.execute_script("return document.title" )
# print(domain_title)

#Write a script to get the URL of the page?
# domain_URL=driver.execute_script("return document.URL" )
# print(domain_URL)

#Write a script to enter the URL?
# driver.execute_script("window.location='http://www.fb.com'")
# time.sleep(5)
time.sleep(5)
#Write a script to open the new tab and enter the URL?
# driver.execute_script("window.open='http://demowebshop.tricentis.com/'")
# time.sleep(5)

#Write a program to scroll down to the bottom of the page?
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(5)

#Write a program to scroll up to the top of the page?
# driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
# time.sleep(5)

#Write a script to scroll to specific element?
comp=driver.find_element(By.XPATH, "//img[@alt='Picture of Build your own computer']")
print(comp)
time.sleep(2)
driver.execute_script(f"{comp.location}.scrollTo();")
# time.sleep(5)

#Write a program to scroll to specific element using the co-ordinate values
# comp=driver.find_element(By.XPATH, "//img[@alt='Picture of Build your own computer']")
# xcordnt=comp.location.get('x')
# ycordnt=comp.location.get('y')
# print(xcordnt,ycordnt)
# time.sleep(5)
# driver.execute_script(f"window.scrollBy({xcordnt},{ycordnt})")
# time.sleep(5)

driver.close()