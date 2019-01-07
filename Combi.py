import time
import getpass
import requests
import pyautogui
from pathlib import Path
from selenium import webdriver

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
driver.get("http://10.135.26.21:8079/siteforge/jsp/index.jsp")
driver.find_element_by_xpath("//*[@class='form-control username']").send_keys('mumbai.cmm')
driver.find_element_by_xpath('//*[@value="Submit"]').click()
time.sleep(0.5)
driver.find_element_by_xpath("//*[@name='j_password']").send_keys('Pass_123')
driver.find_element_by_xpath('//*[@id="Login_button"]').click()
driver.find_element_by_id('rfcSiteSearchTab').send_keys('9496')
driver.find_element_by_xpath('//*[@id="fillterBySiteNameORSapIdDiv"]').click()

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
