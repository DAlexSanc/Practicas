import cv2
import numpy as np

#imagen a grises
imagedata_original = cv2.imread('script4.jpg',0)
cv2.imshow('Original', imagedata_original)


#menoires a 127 a 0 demas a blanco (blanco a mas blanco, negro a mas negro)
ret,threshold_1 = cv2.threshold(imagedata_original, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', threshold_1)
cv2.waitKey(0)

#menores a 127 a 255 (blanco) todo lo demas a 0
ret,threshold_2 = cv2.threshold(imagedata_original, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Binary Inverse', threshold_2)
cv2.waitKey(0)

#Todo pore encima de 127 se redondea a 127 
ret,threshold_3 = cv2.threshold(imagedata_original, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('Threshold Trunc', threshold_3)
cv2.waitKey(0)

#Debajo de 127 a 0 lo demas no se toca
ret,threshold_4 = cv2.threshold(imagedata_original, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('Threshold To Zero', threshold_4)
cv2.waitKey(0)

