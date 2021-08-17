from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="C:\drivers\geckodriver-v0.29.1-win64\geckodriver")
driver.get("https://mydukaan.io/")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div/div/div[2]/a[2]").click()
time.sleep(5)
driver.quit()
