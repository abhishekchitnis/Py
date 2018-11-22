import pyautogui

print(pyautogui.position())

pyautogui.click(131, 751, interval=0.25)
pyautogui.typewrite('Paint', interval=0.1)
pyautogui.click(127, 208, interval=1.25)

import pyautogui
x, y = pyautogui.locateCenterOnScreen('ic.png', grayscale=True)
print(x, y)
pyautogui.click(x, y)
pyautogui.mouseDown(button='left', x=207, y=608)
pyautogui.mouseDown(button='left', x=467, y=283)
pyautogui.mouseDown(button='left', x=849, y=593)
pyautogui.mouseUp(button='left', x=207, y=608)

pyautogui.alert(text='Triangle Drawn, Type Try in TextBox to Continue...', title='Triangle Drawn', button='OK')
pyautogui.password(text='Triangle Drawn, Type Try in TextBox to Continue...', title='Triangle Drawn', default='', mask='*')

# https://pyautogui.readthedocs.io/en/latest/mouse.html
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
