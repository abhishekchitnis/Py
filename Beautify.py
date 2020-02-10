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
print('\n# Welcome # To * Informator *\n\nSystem Name Detected : '+pcnam)
print("\nKindly Share Following Details for Informator to Process the Data and Inform You :) \nYour Full Name : ", end = '')
fnam=input()
print(fnam)
print("Steps Walked FTD : ", end = '')
staps=input()
print(staps)
print("Height (in cm) : ", end = '')
hait=input()
print(hait)
print("Weight : (in kg) : ", end = '')
weit=input()
print(weit)

'''''''''''''''
Path
'''''''''''''''
locate=str(os.getcwd()) #get CWD
print('\n'+'Your Current Working Directory is : '+locate)
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

#driver = webdriver.Chrome(options=opts, executable_path=chrdrv)

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
'''
https://www.calculator.net/bmi-calculator.html
https://www.google.com/search?q=calculate+age+in+python&rlz=1C1GCEV_enIN869IN869&oq=calculate+age+in+python&aqs=chrome..69i57j0l7.7849j0j7&sourceid=chrome&ie=UTF-8&safe=active
https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/
https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python
https://stackoverflow.com/questions/22344244/age-calculator-in-python-from-date-mm-dd-yyyy-and-print-age-in-years-only
https://www.google.com/search?q=pounds+into+kg&rlz=1C1GCEV_enIN869IN869&oq=pounds+in&aqs=chrome.1.69i57j0l7.5424j1j7&sourceid=chrome&ie=UTF-8&safe=active
'''

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""
Py Mains
"""""""""""""""

#driver.get("http://10.135.26.21:8079/siteforge/jsp/login.jsp") # SF URL Load

