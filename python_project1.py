import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0) # Screen Resolution starts from width 0
height= GetSystemMetrics(1) # Captures full screen resolution

dim = (width, height)

f = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("test.mp4", f, 30.0, dim) #Creates a file of name mp4 and frame per second as 30.0 

now_start_time=time.time()
dur = 10+4 #gives the duration of video recording
end_time = now_start_time + dur
while True:
    image = pyautogui.screenshot()  #It takes screenshot
    frame_1 = np.array(image)   # It combines all screenshot to form a video
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break
output.release()

print("--- END ---")
