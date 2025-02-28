import pyautogui
import time


#tt nav to the text space 
time.sleep(2)

def typeFunc(filename, interval=0.01):
    with open(filename, 'r') as file:
        for line in file:
            text = line.strip()
            if text: 
                pyautogui.write(text, interval=interval)
                pyautogui.press('enter')



typeFunc('text.txt')

