import time
import pyautogui
print(pyautogui.size())
pyautogui.hotkey('winleft', 'r')
time.sleep(5)
pyautogui.write('chrome \n')
time.sleep(15)
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('<link> \n')
time.sleep(10)
pyautogui.press('left')
time.sleep(1)
pyautogui.write('\n')
time.sleep(20)
pyautogui.hotkey('win', 'up')
pyautogui.moveTo(850,450, duration = 2.0)
pyautogui.doubleClick()
time.sleep(15)
pyautogui.hotkey('alt', 'r')

