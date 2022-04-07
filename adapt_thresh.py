import cv2
import numpy as np

#imagen a grises
imagedata_original = cv2.imread('script4.jpg',0)
imagedata_original = cv2.medianBlur(imagedata_original,5)
cv2.imshow('Original', imagedata_original)


#Thresh
ret,th1 = cv2.threshold(imagedata_original,127,255,cv2.THRESH_BINARY)
cv2.imshow('Binary', th1)
cv2.waitKey(0)

th2 = cv2.adaptiveThreshold(imagedata_original,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow('Adaptive Mean', th2)
cv2.waitKey(0)

th3 = cv2.adaptiveThreshold(imagedata_original,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow('Gausian', th3)
cv2.waitKey(0)
