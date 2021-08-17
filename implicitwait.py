from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://login.gitam.edu/Login.aspx")

driver.implicitly_wait(10)

assert "GITAM Web Login" in driver.title

driver.find_element_by_name("txtusername").send_keys("321810306033")
driver.find_element_by_name("password").send_keys("yashwant99789@")
driver.find_element_by_name("Submit").click()
