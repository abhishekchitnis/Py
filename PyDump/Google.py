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
driver = webdriver.Chrome(file)
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
