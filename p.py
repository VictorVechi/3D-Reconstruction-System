from unittest import result
import cv2
import numpy as np
def empty():
    pass
image = "imagens/sococo.jpg"
image2 = "imagens/schin2.jpg"

cv2.namedWindow("trackBars")
cv2.resizeWindow("trackBars",640,240)
cv2.createTrackbar("hue min", "trackBars",66,179,empty)
cv2.createTrackbar("hue max", "trackBars",179,179,empty)
cv2.createTrackbar("sat min", "trackBars",6,255,empty)
cv2.createTrackbar("sat max", "trackBars",255,255,empty)
cv2.createTrackbar("val min", "trackBars",100,255,empty)
cv2.createTrackbar("val max", "trackBars",255,255,empty)

while True:
    img = cv2.imread(image)
    img2 = cv2.imread(image)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hMin = cv2.getTrackbarPos("hue min", "trackBars")
    hMax = cv2.getTrackbarPos("hue max", "trackBars")
    sMin = cv2.getTrackbarPos("sat min", "trackBars")
    sMax = cv2.getTrackbarPos("sat max", "trackBars")
    vMin = cv2.getTrackbarPos("val min", "trackBars")
    vMax = cv2.getTrackbarPos("val max", "trackBars")
    print(hMin,hMax,sMin,sMax,vMin,vMax)
    lower = np.array([hMin,sMin,vMin])
    upper = np.array([hMax,sMax,vMax])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    #cv2.imshow("Original",img)
    #cv2.imshow("HSV",imgHSV)
    #cv2.imshow("Mask",mask)
    cv2.imshow("Mask2",imgResult)
    cv2.waitKey(1)   