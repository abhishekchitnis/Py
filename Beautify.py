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
'''
pcnam = getuser()
print('\n# Welcome # To * Informator *\n\nSystem Name Detected : '+pcnam)
print("\nKindly Share Following Details for Informator to Process the Data and Inform You")
print("\nYour Name : ", end = '')
urnam=input()
print(urnam)
'''
try:
	aej = 0
	while not int(aej) in range(1,121):
		aej = input("Age : ")
		print(aej)
	gndr = 1001
	while not int(gndr) in range(0,2):
		gndr = input("Gender : Enter 1 if Male or 0 if Female : ")
		print(gndr)
	staps = 222222
	while not int(staps) in range(0,30000):
		staps = input("Steps Walked throughout the Day : ")
		print(staps)
	hait = 0
	while not int(hait) in range(1,200):
		hait = input("Height (in cm): ")
		print(hait)
	weit = 0
	while not int(weit) in range(1,300):
		weit = input("Weight (in kg): ")
		print(weit)
except:
	print("Wrong Values Entered! Kindly Re-run the Program and Enter Proper Values")
	exit()

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
	print()
	#print('ChromeDriver Present Continuing\n')
else:
	#print('ChromeDriver Absent Downloading\n')
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
Dictionaries
'''''''''''''''''
bmidict = { "<16" : "Severe Thinness",
        "16-17" : "Moderate Thinness",
        "17-18.5" : "Mild Thinness",
        "18.5-25" : "Normal",
        "25-30" : "Overweight",
        "30-35" : "Obese Class I",
        "35-40" : "Obese Class II",
        ">40" : "Obese Class III"
}

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
https://www.calculator.net/bmi-calculator.html
https://www.google.com/search?q=calculate+age+in+python&rlz=1C1GCEV_enIN869IN869&oq=calculate+age+in+python&aqs=chrome..69i57j0l7.7849j0j7&sourceid=chrome&ie=UTF-8&safe=active
https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/
https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python
https://stackoverflow.com/questions/22344244/age-calculator-in-python-from-date-mm-dd-yyyy-and-print-age-in-years-only
https://www.google.com/search?q=pounds+into+kg&rlz=1C1GCEV_enIN869IN869&oq=pounds+in&aqs=chrome.1.69i57j0l7.5424j1j7&sourceid=chrome&ie=UTF-8&safe=active

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""
Py Mains
"""""""""""""""

#driver.get("http://10.135.26.21:8079/siteforge/jsp/login.jsp") # SF URL Load

print('Calculation in Progress..', end='')
sleep(1)
print('..', end='')
sleep(1)
print('..')
sleep(1)
print('\nAnd the Informator has Informed : ')
sleep(1)
cm2m=int(hait)/100
print('\nHeight cm to m : ',cm2m, end='')
bmi=round(int(weit)/(cm2m*cm2m),1)
if bmi<16:
	bmiresult = bmidict["<16"]
elif bmi>=16 and bmi<17:
	bmiresult = bmidict["16-17"]
elif bmi>=17 and bmi<18.5:
	bmiresult = bmidict["17-18.5"]
elif bmi>=18.5 and bmi<25:
	bmiresult = bmidict["18.5-25"]
elif bmi>=25 and bmi<30:
	bmiresult = bmidict["25-30"]
elif bmi>=25 and bmi<35:
	bmiresult = bmidict["30-35"]
elif bmi>=25 and bmi<40:
	bmiresult = bmidict["35-40"]
else:
	bmiresult = bmidict[">40"]
print('\nBMI : ', bmi, 'kg/m\N{SUPERSCRIPT TWO}','(',bmiresult,')', end='')
if gndr==1:
	caco=5
elif gndr==0:
	caco=161

'''
For men:
BMR = 10W + 6.25H - 5A + 5
For women:
BMR = 10W + 6.25H - 5A - 161
'''
#bmr = 10*weit+6.25*hait-5*aej+caco
print('\n * Note * : You Can Consume',bmi,'Calories in a Day to Maintain Your Body Weight', end='')

print('\nDistance Walked : ', round(int(staps)/1400,1), 'Km', end='')
print('\nCalories Burned : ', round(int(staps)*0.04,1), 'Calories', end='')
'''
Ideal Weight : 
Male:	50.0 kg + 2.3 kg per inch over 5 feet
Female:	45.5 kg + 2.3 kg per inch over 5 feet
'''
