'''''''''''''''''''''''
Python Package Imports
'''''''''''''''''''''''
from time import sleep
from datetime import datetime
import os
import ctypes
from getpass import getuser
import requests
import openpyxl
from selenium.webdriver.support.ui import Select
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''''''''''''''''''''
User Input
'''''''''''''''''''''
pcnam = getuser()
print('\nWelcome '+pcnam)

print("Enter Your RJIL Domain ID :")
domainid='Abhishek.Chitnis'#input()
print(domainid)
print("Enter Your RJIL Domain Password :")
password='3m3r#GEN@(y3x1t)'#input()
print(password)

'''''''''''''''
Path
'''''''''''''''
locate=str(os.getcwd()) #get CWD
print(locate)
#locate=locate.replace("\\","/") #Replace Path \''/

'''''''''''''''''''''
Chrome Driver Loads
'''''''''''''''''''''
chrdrv = locate+"/chromedriver.exe"
url = "http://mumbainews24x7.com/Abhishek/chromedriver.exe"
if Path(chrdrv).is_file():
	print('ChromeDriver Present Continuing')
else:
	print('ChromeDriver Absent Downloading')
	r = requests.get(url, stream = True)
	with open(chrdrv, 'wb') as f:
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
#opts.add_argument("--headless")  
driver = webdriver.Chrome(options=opts, executable_path=chrdrv)

"""""""""""""""
Py Functions
"""""""""""""""

'''''''''
Screen
'''''''''
da=datetime.now().strftime('%a_%d-%b-%y')
tim=datetime.now().strftime('%H-%M-%S')
q=1
try:
	os.mkdir(r"Scrs")
except:
	pass
try:
	os.mkdir(r"Scrs/"+da)
except:
	pass

def Scr():
	sleep(1)
	driver.save_screenshot("Scrs/"+da+"/"+tim+".png")

'''''''''''''''
Path
'''''''''''''''
path=str(os.getcwd()) #get CWD
path=path.replace("\\","/") #Replace Path \''/
	
'''''''''''''''
Login / Logout
'''''''''''''''
def Login():
	driver.find_element_by_xpath('//*[@id="content-inner"]/form/input[3]').send_keys(domainid)
	driver.find_element_by_xpath('//*[@id="content-inner"]/form/input[4]').send_keys(password)
	Scr()
	driver.find_element_by_xpath('//*[@id="content-inner"]/form/input[5]').click()
	sleep(5)
	Scr()

def Logout():
	print('Yet to Setup')
	

'''''''''''''''''
Code Func()
'''''''''''''''''
def AttendLinkClick():
	driver.find_element_by_xpath('//*[@id="navmenu"]/li[2]/a').click()
	Scr()
	sleep(3)
	driver.find_element_by_xpath('//*[@id="dropdownMenu1"]/li[1]/a').click()
	Scr()
	sleep(3)
	Scfr()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""
Py Mains
"""""""""""""""
driver.get("http://10.135.26.21:8079/siteforge/jsp/login.jsp") # SF URL Load

driver.get("http://ess.jio.com")
sleep(1)

AttendLinkClick()
