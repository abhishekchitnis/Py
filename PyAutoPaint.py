import pyautogui
import time

print(pyautogui.position())

pyautogui.moveTo(148, 767,0.5)
pyautogui.click(148, 767, interval=0.50)
pyautogui.typewrite('Paint', interval=0.05)
time.sleep(2)
pyautogui.click(157, 263, interval=1.50)
time.sleep(2)
import pyautogui
x, y = pyautogui.locateCenterOnScreen('ic.png', grayscale=True)
print(x, y)
pyautogui.click(x, y)
pyautogui.mouseDown(button='left', x=207, y=608)
pyautogui.mouseDown(button='left', x=467, y=283)
pyautogui.mouseDown(button='left', x=849, y=593)
pyautogui.mouseUp(button='left', x=207, y=608)

pyautogui.alert(text='Triangle Drawn, Type Try in TextBox to Continue...', title='Triangle Drawn', button='OK')
pwd=pyautogui.password(text='Triangle Drawn, Type in TextBox to Continue...', title='Triangle Drawn', default='', mask='*')

print(pwd)

# https://pyautogui.readthedocs.io/en/latest/mouse.html
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
