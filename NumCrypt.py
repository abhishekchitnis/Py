'''''''''''''''''''''''
Python Package Imports
'''''''''''''''''''''''
from time import sleep
from datetime import datetime
import os
import sys
import hashlib
#import ctypes
from getpass import getuser
import requests
#import openpyxl
from pathlib import Path
#from selenium import webdriver
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.chrome.options import Options

'''''''''''''''''''''
User Input
'''''''''''''''''''''
pcnam = getuser()
print('\nWelcome '+pcnam)
'''
print('Smallcell Outdoor for Airspan Automation Started')
try:
    vndor = 0
    while not int(vndor) in range(1,3):
	vndor = input("Enter [1] for Samsung or [2] for Airspan : ")
except:
    print("Wrong Values Entered! Kindly Re-run the Program and Enter Proper Values")
    exit()
'''    
'''''''''''''''
Path
'''''''''''''''
cwdpath=str(os.getcwd()) #get CWD
cwdpath=cwdpath.replace("\\","/") #Replace Path \''/

'''''''''''''''''''''
Chrome Driver Loads
'''''''''''''''''''''
chrdrv = cwdpath+"/chromedriver.exe"

if Path(chrdrv).is_file():
    print('\nChromeDriver Present Continuing')

else:
    print('\nChromeDriver Absent Cannot Continue')
    print("\nPlease Download ChromeDriver and Place it in your CWD :\n\n"+cwdpath+"/")
    input('\nPress [ENTER] to Exit')
    sys.exit()    

'''
else:
    print('\nChromeDriver Absent Downloading')
    url = "http://www.muhurtnews.com/Abhishek/chromedriver.exe"
    r = requests.get(url, stream = True)
    with open(chrdrv, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
'''

'''''''''''
Py Drivers
'''''''''''
'''
opts = Options()
opts.add_argument('start-maximized')
opts.add_argument('disable-infobars')
opts.add_argument('--ignore-certificate-errors')
opts.add_argument("--test-type")
driver = webdriver.Chrome(options=opts, executable_path=chrdrv)
'''
"""""""""""""""
Py Functions
"""""""""""""""

'''''''''
Screen
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

'''''''''''''''
Input
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

""""""""""""""""""""
# A to Z Dict Code 
""""""""""""""""""""
str = ["2", "22", "222", 
       "3", "33", "333", 
        "4", "44", "444", 
        "5", "55", "555", 
        "6", "66", "666", 
        "7", "77", "777", "7777", 
        "8", "88", "888", 
        "9", "99", "999", "9999"]

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ' ':'/', '.':'.-.-.-', ',':'--..--',
    ':':'---...', '?':'..--..', "'":'.----.',
    '-':'-....-', '/':'-..-.', '@': '.--.-.',
    '=':'-...-', '(':'-.--.', ')':'-.--.-',
    '+':'.-.-.'
    }

CODE_REVERSED = {value:key for key,value in CODE.items()}

'''''''''''''''''
Code Func()
'''''''''''''''''
def printSequence(arr, input): 

# length of input string 
    n = len(input) 
    output = "" 

    for i in range(n): 

        # checking for space 
        if(input[i] == ' '): 
            output = output + "0"
        else: 
            # calculating index for each 
            # character		 
            position = ord(input[i]) - ord('A') 
            output = output + arr[position] 
    # output sequence	 
    return output

def to_morse(s):
    return ' '.join(CODE.get(i.upper()) for i in s)

def from_morse(s):
    return ''.join(CODE_REVERSED.get(i) for i in s.split())

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""
Py Mains
"""""""""""""""
#driver.get("http://10.135.26.21:8079/siteforge/jsp/login.jsp") # SF URL Load
#sleep(1)

input = input("\nEnter the Sentence To Encrypt : ").upper()
t9 = printSequence(str, input)
print(t9)

mor = to_morse(t9)	
print("\nReEncrypting T9 to Morse Code : "+mor)

mortohsh = from_morse(mor)

print("\nDecrypting Morse Code to T9 : "+mortohsh.lower())

'''
#driver.close()
#driver.quit()
'''
