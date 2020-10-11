import numpy as np #this program allows to take screenshot evevry 30 seconds for 2 mins
import cv2
import pyautogui
from datetime import datetime
import time

image = pyautogui.screenshot()
mins= 2 #takes screenshot  for 2 mins

tempMins = 0


while tempMins != mins :
    
    title=str(datetime.now())
    x = title.replace(":","-")#certain charecters are not allowed in file names

    image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    cv2.imwrite(x + ".png", image)

    time.sleep(30) #takes screen shot for every 30 seconds
    tempMins +=1
print("over")

    
    
