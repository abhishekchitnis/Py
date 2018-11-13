import time
import getpass
import requests
from pathlib import Path
from selenium import webdriver

user = getpass.getuser()
file = "C:\\Users\\{0}\\Downloads\\chromedriver.exe".format(user)
filechk = Path(file)
url = "http://www.muhurtnews.com/Abhishek/chromedriver.exe"
if filechk.is_file():
	print('Automation Driver Detected -> Automation un Progress...')
else:
    r = requests.get(url, stream = True)
    with open(file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)

driver = webdriver.Chrome(file)
driver.maximize_window()
driver.get("https://ess.jio.com/")

driver.find_element_by_name('username').send_keys('Abhishek.Chitnis')
driver.find_element_by_name('password').send_keys('UIop&*90')
driver.find_element_by_type('submit').click()
time.sleep(5)
driver.find_element_by_link_text('Performance').click()

'''
IMPORTANT NOTEs
'''
# Works for a href Links 
'''
driver.find_element_by_link_text("LinkText").click()
driver.find_element_by_partial_link_text("PartialLinkText").click()
'''
# Works for clickable buttons 
'''
driver.find_element_by_xpath('//button[normalize-space()="BtnTxt"]').click()
'''
# Works for searching elements via name
'''
driver.find_element_by_name('Name')
'''
# EFFECTIVE # Works for searching elements via input type
'''
driver.find_element_by_xpath("//input[@type='InputType']")
'''
