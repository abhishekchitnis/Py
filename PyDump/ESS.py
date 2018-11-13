import time
import getpass
import requests
from pathlib import Path
from selenium import webdriver

user = getpass. getuser()
file = "C:\\Users\\{0}\\Downloads\\chromedriver.exe".format(user)
filechk = Path(file)
url = "http://www.muhurtnews.com/Abhishek/chromedriver.exe"
if filechk.is_file():
	print()
else:
    r = requests.get(url, stream = True)
    with open(file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
print("Enter Your RJIL Domain ID :")
domainid=input()
print("Enter Your RJIL Domain Password :")
password=input()
driver = webdriver.Chrome(file)
driver.maximize_window()
driver.get("https://ess.jio.com/")
driver.find_element_by_xpath('//*[@id="content-inner"]/form/input[3]').send_keys(domainid)
driver.find_element_by_xpath('//*[@id="content-inner"]/form/input[4]').send_keys(password)
driver.find_element_by_xpath('//*[@id="content-inner"]/form/input[5]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="navmenu"]/li[2]/a').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="dropdownMenu1"]/li[1]/a').click()