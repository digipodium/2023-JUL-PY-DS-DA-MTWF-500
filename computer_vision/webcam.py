# pip install opencv-contrin-python pillow mediapipe
import cv2 # library
import numpy as np

CAM_IDX = 0 # 0: default camera
cam = cv2.VideoCapture(CAM_IDX)
while cam.isOpened():
    state, frame = cam.read()
    if not state:
        print('Camera is not available')
        break
    # teen panch yaha se shuru kro
    frame = cv2.flip(frame, 1) # mirror image
    # teen panch yaha pe khatm
    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == 27: # ESC KEY
        break
cam.release()
cv2.destroyAllWindows()