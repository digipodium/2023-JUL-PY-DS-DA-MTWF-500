import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import numpy as np
import time
model_path = 'computer_vision/face_model.tflite'

BaseOptions = mp.tasks.BaseOptions
FaceDetector = mp.tasks.vision.FaceDetector
FaceDetectorOptions = mp.tasks.vision.FaceDetectorOptions
FaceDetectorResult = mp.tasks.vision.FaceDetectorResult
VisionRunningMode = mp.tasks.vision.RunningMode

results = []

def print_result(result: FaceDetectorResult, output_image: mp.Image, timestamp_ms: int):
    results.append(result)

options = FaceDetectorOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)

cam = cv2.VideoCapture(0)
with FaceDetector.create_from_options(options) as detector:
    while True:
        status, img = cam.read()
        ih, iw, _ = img.shape # image height, image width
        if not status:
            print('Camera is not available')
            break
        # teen panch yaha se shuru kro
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img)
        frame_timestamp_ms = int(time.time() * 1000)
        detector.detect_async(mp_image, frame_timestamp_ms)

        if results:
            result = results.pop()
            if result.detections:
                for detection in result.detections:
                    # print(detection.keypoints)
                    x = detection.bounding_box.origin_x
                    y = detection.bounding_box.origin_y
                    w = detection.bounding_box.width
                    h = detection.bounding_box.height
                    cv2.rectangle(img, (x-20, y-20), (x+w+20, y+h+20), (0, 255, 0), 2)
                    for keypoints in detection.keypoints: # extract all keypoints   
                        nx = keypoints.x
                        ny = keypoints.y
                        x = int(nx * iw) # convert normalized value to pixel value
                        y = int(ny * ih) # convert normalized value to pixel value
                        cv2.circle(img, (x, y), 2, (0, 0, 255), 2) # draw circle
        # teen panch yaha pe khatm
        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == 27: # ESC KEY
            break
    cam.release()
    cv2.destroyAllWindows()