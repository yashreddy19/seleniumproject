from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://login.gitam.edu/Login.aspx")

userele=driver.find_element_by_name("txtusername")
print(userele.is_enabled())
print(userele.is_displayed())

password=driver.find_element_by_name("password")
print(password.is_enabled())
print(password.is_displayed())

userele.send_keys("321810306033")
password.send_keys("yashwant99789@")

driver.find_element_by_name("Submit").click()

time.sleep(7)

driver.quit()




