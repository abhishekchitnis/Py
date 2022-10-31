# Paint Draw Hut with Spiral Garage by Abhi

#Importing Packages
import pyautogui
from time import sleep

#Wait for No Reason
sleep(2)

#Display Mouse Position for No Reason
print(pyautogui.position())

#Open Paint for Some Reason
pyautogui.press('win')
pyautogui.typewrite('Paint', interval=0.05)
sleep(1)
pyautogui.press('enter')

#Wait for No Reason
sleep(2)

#Move Mouse To Position For Some Reason
pyautogui.moveTo(226, 326)  

#Clicking Mouse For XYZ Reason
pyautogui.click()  # using .click() method to click
l = 200 # setting values for no reason
a = 4 # setting values for no reason
x, y = pyautogui.position() # noting mouse position for some reason
  
#Making a Square First

pyautogui.dragRel(200, 0, 0.2)
x1, y1 = pyautogui.position()
a -= 1
pyautogui.dragRel(0, 200, 0.2)
a -= 1
pyautogui.dragRel(-200, 0, 0.2)
a -= 1
pyautogui.dragRel(0, -200, 0.2)
a -= 1
  
#Making a Triangle Over the Square
pyautogui.click(x, y)
pyautogui.dragRel(100, -100, 0.2)
pyautogui.click(x1, y1)
pyautogui.dragRel(-100, -100, 0.2)
  
#Making Rest of the Body of the Hut
pyautogui.dragRel(350, 0, 0.2)
pyautogui.dragRel(0, 300, 0.2)
pyautogui.dragRel(-290, 0, 0.2)
pyautogui.click(x1, y1)
pyautogui.dragRel(250, 0, 0.2)

#Clicking and Setting Distance
pyautogui.click()
distance = 200

#Adding Spiral Garage for No Reason
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2) # move down

    pyautogui.dragRel(-distance, 0, duration=0.2) #move left
    distance = distance - 5

    pyautogui.dragRel(0, -distance, duration=0.2) #move up

# https://pyautogui.readthedocs.io/en/latest/mouse.html
# https://pyautogui.readthedocs.io/en/latest/keyboard.html