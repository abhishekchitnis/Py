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
#from SF2 import driver

'''''''''''''''''''''
User Input
'''''''''''''''''''''
pcnam = getuser()
print('\nWelcome '+pcnam)

wb = openpyxl.load_workbook("SCOImport.xlsx", data_only=True) 
sapid = wb['Sheet1']['U2'].value
print("\nSAP ID : "+sapid)
'''
print('\nEnter SAP ID: ')
sapid=input()
print('\nSelect which Band to Perform: \n\n1. 2300\n2. 1800\n3. 850 \n\nChoose 1/2/3 : ')
sel=input()
if sel>'3' or sel<'1':
	print("\nPlease Choose Between 1 to 3 only")
	input("\nPress [ENTER] to Exit")
	exit()
'''

'''''''''''''''''''''
Chrome Driver Loads
'''''''''''''''''''''
chrdrv = cwdpath+"/chromedriver.exe"
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
cwdpath=str(os.getcwd()) #get CWD
print(cwdpath)
cwdpath=cwdpath.replace("\\","/") #Replace Path \''/

'''''''''''''''
Login / Logout
'''''''''''''''
def Login():
	driver.find_element_by_xpath("//*[@class='form-control username']").send_keys(user)
	driver.find_element_by_xpath('//*[@value="Submit"]').click()
	sleep(1)
	driver.find_element_by_xpath("//*[@name='j_password']").send_keys('Pass_123')
	driver.find_element_by_xpath('//*[@id="Login_button"]').click()
	Scr()

def Logout():
	driver.find_element_by_xpath('//*[@id="user-nameco"]').click()
	sleep(1)
	driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/ul/li[3]/a/span').click()

'''''''''''''''''
Code Func()
'''''''''''''''''
def AssBtn():
	driver.find_element_by_xpath('//*[@id="smallcell_out_Atp_11A_task_list_table"]/tbody/tr[2]/td[7]/a').click()
	Scr()
	
def MKAVen():
	driver.find_element_by_xpath('//*[@id="smallcell_atp11A_task_vendors"]').send_keys('Innoeye')
	Scr()
	driver.find_element_by_xpath('//*[@id="smallcell_atp11A_task_vendorPm"]').send_keys('Amol Gupta')
	Scr()
	driver.find_element_by_xpath('//*[@id="smallcellOut_atp11A_assignTaskToPMButton"]').click()
	Scr()

def AssOKBtn():
	driver.find_element_by_xpath('//*[@id="smallcell_out_Atp_11A_task_list_table"]/tbody/tr[2]/td[7]/a[1]').click()
	Scr()
	driver.find_element_by_xpath('//*[@id="smallcell_Out_ATP11A__accept_task_modal"]/div/div[3]/button[2]').click()
	Scr()

def TskSrchSAP():
	driver.find_element_by_xpath('//*[@id="smallcell_out_atp11a_task_li"]/a').click()
	Scr()
	driver.find_element_by_xpath('//*[@id="smallcell_out_atp_11_A_list_taskSiteSearch"]').send_keys(sapid)
	Scr()
	driver.find_element_by_xpath('//*[@id="small_cell_atp_11_A_TaskSearchTab"]/button').click()
	Scr()

def SCOOdd():
	driver.find_element_by_xpath('//*[@id="import_site_btn_title"]').click()
	Scr()
	driver.find_element_by_xpath("//*[@id='fileUploadInput']").send_keys(path+"/SCOOddSamsung.xlsx") #Upload File
	Scr()
	driver.find_element_by_xpath('//*[@id="smc_out_atp11a_site_triggerUpload"]').click()
	Scr()	

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""
Py Mains
"""""""""""""""
driver.get("http://10.135.26.21:8079/siteforge/jsp/login.jsp") # SF URL Load
sleep(1)

'''
'''''''''''''''''''''''''''''''''''''''''''''''''''
# Smallcell.Admin
'''''''''''''''''''''''''''''''''''''''''''''''''''
#Import Site
user = 'smallcell.admin' #SF Smallcell Outdoor Admin
Login()
sleep(1)
try:
	driver.find_element_by_xpath('//*[@id="small_cell_site_data_upload_modal"]').click() # Click Import Site
	Scr()
	driver.find_element_by_xpath("//*[@id='fileUploadInput']").send_keys(cwdpath+"/SCOImport.xlsx") #Upload File
	Scr()
	driver.find_element_by_xpath('//*[@id="small_cell_site_triggerUpload"]').click() # Click Upload # Commented for Uploading
	Scr()
	
	#Direct ATP 11A
	driver.find_element_by_xpath('//*[@id="small_cell_atp11A_trigger_data_upload_modal"]').click() # Click ATP Trigger
	Scr()
	driver.find_element_by_xpath("//*[@id='fileUploadInput']").send_keys(cwdpath+"/SCOATP11A.xlsx") #Upload File
	Scr()
	driver.find_element_by_xpath("//input[@id='small_cell_atp11A_task_triggerUpload']").click() # Click Upload # Commented for Uploading
	Scr()
except:
	pass
Logout()

'''''''''''''''''''''''''''''''''''
# Manoj.Kumar
'''''''''''''''''''''''''''''''''''
user = 'manoj.kumar' #SF Smallcell Outdoor Lead
Login()
sleep(1)
driver.find_element_by_xpath('//*[@id="smallcell_out_atp11a_site_li"]/a').click()
Scr()
driver.find_element_by_xpath('//*[@id="smallcellOut_atp11A_site_by_name"]').send_keys(sapid)
Scr()
driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/button').click()
Scr()
try:
	driver.find_element_by_xpath('//*[@id="smallcellOut_atp11A_site_list_table"]/tbody/tr[2]/td[5]/a').click()
	Scr()
	driver.find_element_by_xpath('//*[@id="jcEngg"]').send_keys('sachin gupta')
	Scr()
	driver.find_element_by_xpath('//*[@id="smallcell_out_site_assign_to_jc_engineer_modal"]/div/div[3]/a').click()
	Scr()
except:
	pass

TskSrchSAP()
try:
	AssBtn()
	MKAVen()
	driver.find_element_by_xpath('//*[@id="smallcell_out_Atp_11A_task_list_table"]/tbody/tr[3]/td[7]/a').click()
	Scr()
	MKAVen()
except:
	pass
Logout()

'''''''''''''''''''''''''''''''''''
# Amol.Gupta
'''''''''''''''''''''''''''''''''''
user = 'amol.gupta' #SF Smallcell Vendor PM
Login()
sleep(1)
TskSrchSAP()

# Task 1 Equip Inst/Exec ATP11A
try:
	AssBtn()
	driver.find_element_by_xpath('//*[@id="smallcell_Atp11A_task_vendorFE"]').send_keys('Rahul Patidar')
	Scr()
	driver.find_element_by_xpath('//*[@id="smallcell_Atp11A_assignTaskToFeButton"]').click()
	Scr()
except:
	pass

# Task 2 Equip Inst/Exec ATP11A
try:
	driver.find_element_by_xpath('//*[@id="smallcell_out_Atp_11A_task_list_table"]/tbody/tr[3]/td[7]/a').click()
	Scr()
	driver.find_element_by_xpath('//*[@id="smallcell_Atp11A_task_vendorFE"]').send_keys('Rahul Patidar')
	Scr()
	driver.find_element_by_xpath('//*[@id="smallcell_Atp11A_assignTaskToFeButton"]').click()
	Scr()	
except:
	pass
Logout()

'''''''''''''''''''''''''''''''''''
# Rahul.Patidar
'''''''''''''''''''''''''''''''''''
user = 'rahul.patidar' #SF Smallcell FE
Login()
sleep(1)
TskSrchSAP()
sleep(2)
Logout()
ctypes.windll.user32.MessageBoxExW(0, 'Please Perform FE Task Manually as per Requirement and then Press [OK]', 'Khud Se Bharo', 0x1000)

'''''''''''''''''''''''''''''''''''
# Amol.Gupta
'''''''''''''''''''''''''''''''''''
user = 'amol.gupta' #SF Smallcell Vendor PM
Login()
sleep(1)
TskSrchSAP()
try:
	AssOKBtn()
except:
	pass
Logout()

'''''''''''''''''''''''''''''''''''
# Sachin.Gupta
'''''''''''''''''''''''''''''''''''
user = 'sachin.gupta' #SF Smallcell Vendor PM
Login()
sleep(1)
TskSrchSAP()
try:
	AssOKBtn()
except:
	pass
Logout()

'''''''''''''''''''''''''''''''''''
# Manoj.Kumar
'''''''''''''''''''''''''''''''''''
user = 'manoj.kumar' #SF Smallcell Outdoor Lead
Login()
sleep(1)
TskSrchSAP()
try:
	AssOKBtn()	
except:
	pass
Logout()

'''
'''''''''''''''''''''''''''''''''''
# Mum NPE
'''''''''''''''''''''''''''''''''''
user = 'mum.npe' #SF Smallcell Outdoor Lead
Login()

#try:
SCOOdd()
errmsg = driver.find_element_by_xpath('//*[@id="smc_out_atp11a_site_import_message"]')
while errmsg.is_displayed():
	print ("\n"+str(errmsg))
	ctypes.windll.user32.MessageBoxExW(0, 'Error while Uploading ODD, Kindly Check and Repair Excel and Press [OK] to Re-Upload', 'Thik Se Bharo', 0x1000)
	driver.find_element_by_xpath('//*[@id="smc_out_atp11a_site_file_upload_modal"]/div/div[1]/button').click()
	SCOOdd()
driver.find_element_by_xpath('//*[@id="gritter-item-2"]/div[2]/div[1]/span')

print ("\nSCO Odd For Samsung Successfully Uploaded")
	
#except:
#	print('\nError while Uploading ODD, Kindly Check and Re-Run the Script')	
#Logout()

#driver.close()
#driver.quit()
