import pyautogui
import cv2
import time

buttons = []
firstLoop = True
pyautogui.pause = 0.001
locS = pyautogui.locateCenterOnScreen('assets\\Senna.png')
locV = pyautogui.locateCenterOnScreen('assets\\Viego.png')
locN = pyautogui.locateCenterOnScreen('assets\\Nidalee.png')
locA = pyautogui.locateCenterOnScreen('assets\\Aatrox.png')
locT = pyautogui.locateCenterOnScreen('assets\\Terminal.png')

while True:
    if(firstLoop):
        inp = int(input('Next panel: '))
        buttons.append(inp)
        inp = int(input('Next panel: '))
        buttons.append(inp)
        firstLoop = False
    inp = int(input('Next panel: '))
    buttons.append(inp)
    print(buttons)
    for button in buttons:
        time.sleep(0.001)
        if button == 1:
            pyautogui.moveTo(locS)
            pyautogui.click()
        elif button == 2:
            pyautogui.moveTo(locV)
            pyautogui.click()
        elif button == 3:
            pyautogui.moveTo(locN)
            pyautogui.click()
        elif button == 4:
            pyautogui.moveTo(locA)
            pyautogui.click()
    pyautogui.moveTo(locT)
    pyautogui.click()