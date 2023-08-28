import cv2
import numpy as np

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
cv2.namedWindow('cameras') # required
cv2.createTrackbar('minimum', 'cameras', 0, 255, lambda x: None)
cv2.createTrackbar('maximum', 'cameras', 0, 255, lambda x: None)
bs = cv2.createBackgroundSubtractorKNN()
while True:
    st1, img1 = cam1.read()
    st2, img2 = cam2.read()
    out = np.hstack((img1, img2))
    # edge detection
    min = cv2.getTrackbarPos('minimum', 'cameras')
    max = cv2.getTrackbarPos('maximum', 'cameras')
    outline = cv2.Canny(out, min, max, 3)
    inverted = cv2.bitwise_not(outline)
    cv2.imshow("cameras", inverted)
    # background subtraction
    mask = bs.apply(img2)
    fg = cv2.bitwise_and(img2, img2, mask=mask)
    cv2.imshow("mask", mask)
    cv2.imshow("fg", fg)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cam1.release()
cam2.release()
cv2.destroyAllWindows()