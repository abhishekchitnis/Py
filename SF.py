'''''''''''''''''''''''
Python Package Imports
'''''''''''''''''''''''
import time
from datetime import datetime
import os
import getpass
import requests
import pyautogui
import openpyxl
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

'''''''''''''''''''''
User Input
'''''''''''''''''''''
pcnam = getpass.getuser()
print('\nWelcome '+pcnam)
print('\nEnter SAP ID: ')
sapid=input()

'''''''''''''''''''''
Chrome Driver Loads
'''''''''''''''''''''
chrdrv = "C:\\Users\\{0}\\Downloads\\chromedriver.exe".format(pcnam)
url = "http://www.muhurtnews.com/Abhishek/chromedriver.exe"
if Path(chrdrv).is_file():
	print()
else:
	r = requests.get(url, stream = True)
	with open(file, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			f.write(chunk)

'''''''''''
Py Drivers
'''''''''''
opts = Options()
opts.add_argument('start-maximized')
opts.add_argument('disable-infobars')
opts.add_argument('--ignore-certificate-errors')
opts.add_argument("--test-type")
driver = webdriver.Chrome(options=opts, executable_path=chrdrv)

"""""""""""""""
Py Functions
"""""""""""""""

'''''''''
Screen
'''''''''
datim=datetime.now().strftime('%a_%d-%b-%y_%H-%M')
q=1
def Scr():
	driver.save_screenshot("Scrs/"+datim+"_"+str(q)+".png")
'''''''''''''''
Login / Logout
'''''''''''''''
def Login():
	driver.find_element_by_xpath("//*[@class='form-control username']").send_keys(user)
	driver.find_element_by_xpath('//*[@value="Submit"]').click()
	time.sleep(1)
	driver.find_element_by_xpath("//*[@name='j_password']").send_keys('Pass_1234')
	driver.find_element_by_xpath('//*[@id="Login_button"]').click()
	time.sleep(1)

def Logout():
	driver.find_element_by_xpath('//*[@id="user-nameco"]').click()
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/ul/li[3]/a/span').click()
	time.sleep(1)

"""""""""""""""
Py Mains
"""""""""""""""
driver.get("http://10.135.26.21:8079/siteforge/jsp/login.jsp")

'''''''''''''''''''''''''''''''''
RFI Survey Tasks - Shubhendu.B (CM)
'''''''''''''''''''''''''''''''''
user='shubhendu.b'
Login()
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_survey_li"]/a').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiSurveyFrequencyFilter"]').send_keys('2300')
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_id('rfiSiteNameForFilter2300').send_keys(sapid)
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiStatusForFilterDiv2300"]/button').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_task_div_table_2300"]/tbody/tr/td[7]/a').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_area_manager_2300"]').send_keys('chunnilal')
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="assignToAmBtn_2300"]').click() #Commented for Assignment
Scr()
q=q+1
Scr()
q=q+1
Logout()

'''''''''''''''''''''''''''''''''
RFI Survey Tasks - Chunnilal.D (AM)
'''''''''''''''''''''''''''''''''
user='chunnilal.d'
Login()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_survey_li"]/a').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiSurveyFrequencyFilter"]').send_keys('2300')
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiSiteNameForFilter2300"]').send_keys(sapid)
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiStatusForFilterDiv2300"]/button').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_task_div_table_2300"]/tbody/tr/td[7]/a').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="samsungSolParForRfi_2300.username"]').send_keys('Wipro Ltd')
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="samsungProjectManagerForRfi_2300.username"]').send_keys('Anoop Kumar')
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="assign_pm_for_rfi_btn_2300"]').click() #Commented for Assignment
time.sleep(1)
Scr()
q=q+1
Logout()

'''''''''''''''''''''''''''''''''
RFI Survey Tasks - Anoop Kumar (PM)
'''''''''''''''''''''''''''''''''
user='anoop.k'
Login()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_survey_li"]/a').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiSurveyFrequencyFilter"]').send_keys('2300')
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiSiteNameForFilter2300"]').send_keys(sapid)
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiStatusForFilterDiv2300"]/button').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_task_div_table_2300"]/tbody/tr/td[7]/a').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_field_engineer_2300"]').send_keys('sanjay FE')
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="assignRFIFEButton_2300"]').click() #Commented for Assignment
time.sleep(1)
Scr()
q=q+1
Logout()


'''
user='chunnilal.d'
Login()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_survey_li"]/a').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiSurveyFrequencyFilter"]').send_keys('2300')
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiSiteNameForFilter2300"]').send_keys(sapid)
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfiStatusForFilterDiv2300"]/button').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="rfi_task_div_table_2300"]/tbody/tr[1]/td[7]/a[3]').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="accepetedByAMWithGO"]').click()
time.sleep(1)
Scr()
q=q+1
driver.find_element_by_xpath('//*[@id="areaManagerAcceptanceModalSubmitButton2300"]').click() #Commented for Assignment
time.sleep(1)
Scr()
q=q+1
Logout()
'''

driver.close()
driver.quit()
