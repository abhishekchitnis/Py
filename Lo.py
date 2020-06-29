from selenium import webdriver
# from selenium.webdriver.common.keys import keys
driver= webdriver.Chrome(executable_path="C:/Users/Abhishek.Chitnis/Downloads/chromedriver.exe")
driver.get("file:///C:/Users/Abhishek.Chitnis/Desktop/hi.html");
print(driver.title)
print(driver.current_url)
print(driver.page_source)
print(driver.close)
