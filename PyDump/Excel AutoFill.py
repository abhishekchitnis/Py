import time
import getpass
import requests
import openpyxl
from pathlib import Path
from selenium import webdriver

wb = openpyxl.load_workbook("! EDIT ME.xlsx", data_only=True) 

weblink = wb['AutoData']['D2']

print("{0}".format(wb['AutoData']['D2']))
input1=input()

print("{0}".format(wb['AutoData']['D2']))
input2=input()

print("{0}".format(wb['AutoData']['D2']))
input3=input()

print("{0}".format(wb['AutoData']['D2']))
input4=input()

print("{0}".format(wb['AutoData']['D2']))
input5=input()

user = getpass.getuser()
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

driver = webdriver.Chrome(file)
driver.maximize_window()
driver.get("{0}".format(weblink.value))
driver.find_element_by_xpath('//*[@id="jazz_app_internal_LoginWidget_0_userId"]').send_keys(un.value)
driver.find_element_by_xpath('//*[@id="jazz_app_internal_LoginWidget_0_password"]').send_keys(pw.value)
driver.find_element_by_xpath('//*[@id="jazz_app_internal_LoginWidget_0"]/div[1]/div[1]/div[3]/form/button').click()
driver.find_element_by_xpath('//*[@id="jazz_ui_SearchBox_0"]/form/div/div/div/input').send_keys(fdid)
driver.find_element_by_xpath('//*[@id="jazz_ui_SearchBox_0"]/form/div/a').click()
