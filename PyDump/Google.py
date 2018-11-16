import time
import getpass
import requests
from pathlib import Path
from selenium import webdriver

user = getpass. getuser()
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

cos = webdriver.ChromeOptions()
#cos.add_argument('--disable-gpu')
#cos.add_argument('--kiosk')
#cos.add_argument('--window-position=0,0')
cos.add_argument('--disable-infobars');
			
driver = webdriver.Chrome(executable_path=file, options=cos)
driver.maximize_window()

driver.get("http://www.google.com")

# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium Automation using Python")
search_field.submit()

# get the list of elements which are displayed after the search
# currently on result page using find_elements_by_class_name method
stats=driver.find_element_by_xpath('//*[@id="resultStats"]').text

# get the number of elements found
print("\n",stats)

# close the browser window
driver.quit()


'''
--------------------
Try This if Warning ChromeDriver
--------------------
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
--------------------
https://github.com/SeleniumHQ/selenium/issues/5966
--------------------
'''
