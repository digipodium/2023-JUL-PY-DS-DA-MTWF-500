import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import numpy as np
import time

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

results = []
model_path = r'computer_vision\gesture_recognizer.task'
cam = cv2.VideoCapture(0)

base_options = BaseOptions(model_asset_path=model_path)
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    results.append(result)

def show_on_window(window, text, img):
    cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 255, 0), 2)
    cv2.imshow(window, img)

def draw_hand_landmarks(img, x, y, z):
    # display depth using size with filled circle
    print(int(abs(z)/3))
    s = int(abs(z)/3) if int(abs(z)/3) > 3 else 3
    cv2.circle(img, (x, y), s, (0, 255, 255), -1)

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with GestureRecognizer.create_from_options(options) as recognizer:
    while True:
        status, img = cam.read()
        ih, iw, _ = img.shape # image height, image width
        if not status:
            print('Camera is not available')
            break
        # teen panch yaha se shuru kro
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)
        frame_timestamp_ms = int(time.time() * 1000)
        recognizer.recognize_async(mp_image, frame_timestamp_ms)

        if results:
            result = results.pop()
            if result.gestures:
                for gesture in result.gestures:
                    name = gesture[0].category_name
                    score = gesture[0].score
                    display_name = f"{name} ({round(score,2)})"
                    show_on_window('Webcam', display_name, img)
            if result.hand_landmarks:
                for landmarks in result.hand_landmarks:
                    for landmark in landmarks:
                        x = int(landmark.x * iw)
                        y = int(landmark.y * ih)
                        z = int(landmark.z * iw)
                        draw_hand_landmarks(img, x, y, z)
                
                    
        # teen panch yaha pe khatm
        cv2.imshow('Webcam', img)
        if cv2.waitKey(10) == 27: # ESC KEY
            break
    cam.release()
    cv2.destroyAllWindows()

