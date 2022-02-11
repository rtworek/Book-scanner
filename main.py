import pyautogui
import tkinter as tk
#from tkinter.filedialog import *
import time
x1, y1 = 300, 100
x2, y2 = 1620, 1035

root = tk.Tk()
#root.attributes('-fullscreen', True)
canvas1 = tk.Canvas(root, width = 100, height = 50)
canvas1.pack()

class Region:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

class Scanner:
    def __init__(self):
        self.type = 'Region_scanner'


def takeScreenshot(i = 0):
    myScreenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    myScreenshot = myScreenshot.convert('RGB')
    #save_path = asksaveasfilename()
    save_path = "J:/Python_projects/pythonProject/BookScanner/Alpine_Handbook/"
    if 0 <= i < 10:
        filename = "00" + str(i) + "_AlpineHandbook.pdf"
    elif 10 <= i < 100:
        filename = "0" + str(i) + "_AlpineHandbook.pdf"
    else:
        filename = str(i) + "_AlpineHandbook.pdf"

    myScreenshot.save(save_path + filename)
    print(save_path + filename)

def scanBook():
    pyautogui.moveTo(50, 330)
    pyautogui.click()
    for i in range(338):
        takeScreenshot(i)
        pyautogui.press('right')
        time.sleep(2)


#while True:
#    x, y = pyautogui.position()
#    print(x, y)

myButton = tk.Button(text="Scan book", command = scanBook, font=10)
canvas1.create_window(50, 25, anchor='center', window=myButton)
root.mainloop()

#img = pyautogui.screenshot(region=(200, 200, 300, 400))