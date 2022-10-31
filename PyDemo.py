"""""""""""""""
Py Imports
"""""""""""""""
import os
from getpass import getuser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from time import sleep

'''''''''''''''
Chr Drv Path
'''''''''''''''
cwdpath = str(os.getcwd()) #get CWD
cwdpath = cwdpath.replace("\\","/") #Replace Path \''/
chrdrv = cwdpath+"/chromedriver.exe"

'''''''''''''''''
Chr Drv Options
'''''''''''''''''
opts = webdriver.ChromeOptions(); 
opts.add_argument('start-maximized')
opts.add_argument('disable-infobars')
opts.add_experimental_option("excludeSwitches", ['enable-automation']);
opts.add_argument('--ignore-certificate-errors')
opts.add_argument("--test-type")

'''''''''''''''''
Chr Drv Set
'''''''''''''''''
driver = webdriver.Chrome(options=opts, executable_path=chrdrv)

'''''''''
Snaps
'''''''''
da=datetime.now().strftime('%a_%d-%b-%y')
tim=datetime.now().strftime('%H-%M-%S')
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

'''''''''''''''''
Code Func()
'''''''''''''''''
def BtnClk():
    print(d.text)
    d.click()
    sleep(2)
    driver.back()

def BtnClk2():
    sleep(2)
    print(f.text)
    f.click()

'''''''''''''''''''''
Sample While Loop
'''''''''''''''''''''
i = 1
while i < 3:
  print(i)
  i += 1
print('\n')

"""""""""""""""
Py Mains
"""""""""""""""

'''''''''''''''''
Load URL
'''''''''''''''''
driver.get("https://ultimateqa.com/simple-html-elements-for-automation/") # URL Load
sleep(1)

'''''''''''''''''
Drv Operations
'''''''''''''''''
d = driver.find_element('xpath','//*[@id="button1"]')
BtnClk()

d = driver.find_element('xpath','//*[@id="button2"]')
BtnClk()

f = driver.find_element('xpath','//*[@id="idExample"]')
BtnClk2()
sleep(2)
g = driver.find_element('xpath','//*[@id="post-4690"]/div[1]/h1')
print(g.text)
driver.back()
print("Done Now\n")

f = driver.find_element(By.LINK_TEXT,'Click me using this link text!')
BtnClk2()
sleep(2)
g = driver.find_element(By.XPATH,'//*[@id="post-4705"]/div[1]/h1')
print(g.text)
driver.back()
print("Done How\n")

f = driver.find_element(By.CLASS_NAME,'buttonClass')
BtnClk2()
sleep(2)
g = driver.find_element('xpath','//*[@id="post-4690"]/div[1]/h1')
print(g.text)
driver.back()
print("Done Wow\n")

'''''''''''''''''
Close/Quit Drv
'''''''''''''''''
driver.close()
driver.quit()
