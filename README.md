# record-a-zoom-meeting
Run this file in python to automate the process of Recording a Zoom Meeting as a Host
===================================
#Setup
========================================
Edit ```link``` to the link of your meeting<br>
Here :
```
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('<link> \n')
time.sleep(10)
```
#Modules Required
====================================
```pyautogui```
and ```time``` <br>
Time is pre-installed with Python
Install PyAutoGui by typing
```pip3 install pyautogui``` or ```pip install pyautogui```
