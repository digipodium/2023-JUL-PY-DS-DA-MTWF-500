# pip install opencv-contrin-python pillow mediapipe
import cv2 # library
import numpy as np

VIDEO_PATH = r"C:\Users\ZAID\Videos\u4.exe\vid.mp4" # 0: default camera
cam = cv2.VideoCapture(VIDEO_PATH)
while cam.isOpened():
    state, frame = cam.read()
    if not state:
        print('Video is not available')
        break
    frame = cv2.resize(frame, None, fx=.5, fy=.5)
    # teen panch yaha pe khatm
    cv2.imshow('video', frame)
    if cv2.waitKey(10) == 27: # ESC KEY
        break
cam.release()
cv2.destroyAllWindows()