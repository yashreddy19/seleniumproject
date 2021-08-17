from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver-v0.29.1-win64\geckodriver")
driver.get("https://mydukaan.io/")
print(driver.title)
driver.get("https://login.gitam.edu/Login.aspx")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
time.sleep(5)
driver.quit()