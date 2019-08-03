''' Refer : Drv Arg by Abhi '''

#Import Packages 
import time
import getpass
import requests
import pyautogui
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Check and Load/Download Chrome Driver Code
user = getpass.getuser()
chrdrv = "C:\\Users\\{0}\\Downloads\\chromedriver.exe".format(user)
url = "http://www.muhurtnews.com/Abhishek/chromedriver.exe"
if Path(chrdrv).is_file():
	print()
else:
    r = requests.get(url, stream = True)
    with open(chrdrv, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
			
# WebDriver Options
opts = Options()
opts.add_argument('start-maximized')
opts.add_argument('disable-infobars')
driver = webdriver.Chrome(options=opts, executable_path=chrdrv)

# WebDriver URL Load
driver.get("http://www.google.com")

# Locate the Search TextBox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# Enter Search Keyword and Submit
search_field.send_keys("Selenium Automation using Python")
search_field.submit()

# Get the List of Elements which are Displayed After the Search
stats=driver.find_element_by_xpath('//*[@id="resultStats"]').text

# Dislay the Number of Elements Found
print("\n",stats)

# Close the Browser Window
driver.quit()


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


'''-----------------------------
Try This if Warning ChromeDriver
--------------------------------
I just manually created the missing registry key and it stopped logging that.

 @lortegas
lortegas commented on Jun 18
Jarmake... How did you do it?

 @gittadesushil
gittadesushil commented on Jun 18
Please share the steps to add registry key.

 @jarmake
jarmake commented on Jun 19 • 
Ok.

Open registry with regedit (just click on Windows start menu and start typing regedit, it should come up)
From the registry explorer, expand HKEY_LOCAL_MACHINE, and from there expand SOFTWARE
Expand Policies.
I was missing everything from this point.
So what I had to do was to select the Policies by left clicking on it, and then right click and from the context menu select New > Key and name it Google.
Once that is created, select that and right click and again select New > Key and name that Chrome.
Select that folder, and right click. Choose New > String. Name it as MachineLevelUserCloudPolicyEnrollmentToken and leave the value empty.
If you alreade have Google and Chrome under Policies, I think only adding the key as in step 6 should work. I've attached a picture to show how it should look like when it's done.
And just as a clarifier. This is under SOFTWARE/Policies, not directly under SOFTWARE.
---------------------------------------------------
https://github.com/SeleniumHQ/selenium/issues/5966
-------------------------------------------------'''