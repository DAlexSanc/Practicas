#Librerias 
import cv2
import numpy as np
import matplotlib.pyplot as plt
from picamera import PiCamera

#definicion de camara 
#camera = PiCamera ()

#Captura
#camera.start_preview()
#camera.capture('/home/pi/Desktop/gold.jpg')
#cv2.waitKey(0)
#camera.capture('/home/pi/Desktop/defect.jpg')
#cv2.waitKey(0)
#camera.stop_preview()

def medidas (imagen):
    print('Tamano =', imagen.shape)
    print('Alto =', imagen.shape[0])
    print('Ancho =', imagen.shape[1])
    print('Valor max =', np.max(imagen))
    print('Valor min =', np.min(imagen))

image1 = cv2.imread('img.png')
image2 = cv2.imread('img.png')

#YIQ

Gimage = np.zeros(image1.shape,np.uint8)
for i in range (image1.shape[0]): #recorre filas
    for j in range (image1.shape[1]): # recorre columnas
        Gimage[i,j] = (image1[i,j,2]*0.299 + image1[1,j,1]*0.587 + image1[i,j,0]*0.114)

Dimage = np.zeros(image2.shape,np.uint8)
for i in range (image2.shape[0]): #recorre filas
    for j in range (image2.shape[1]): # recorre columnas
        Dimage[i,j] = (image2[i,j,2]*0.299 + image2[1,j,1]*0.587 + image2[i,j,0]*0.114)

medidas (Gimage)
medidas (Dimage)

cv2.imshow('A yiq g',Gimage)
cv2.imshow('A yiq d',Dimage)
cv2.waitKey(0)
cv2.destroyAllWindows()


#A grises 

#Ggray = cv2.cvtColor(Gimage, cv2.COLOR_BGR2GRAY)
#Dgray = cv2.cvtColor(Dimage, cv2.COLOR_BGR2GRAY)

#cv2.imshow('Golden', Ggray)
#cv2.imshow('Defective', Dgray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Histogram
rango = [0,256]
valores = 256
valG, ranG = np.histogram(Gimage,valores, rango)
conteoG = ranG[:-1]

valD, ranD = np.histogram(Dimage,valores, rango)
conteoD = ranD[:-1]

def histograma (ejeX, imagen):
    fig, ax = plt.subplots(figsize=(8,8))
    plt.bar(ejeX, imagen, width=imagen.shape[0] / (ejeX[-1] - ejeX[0] + 1))
    return fig, ax 

histograma(conteoG, valG)
plt.title("Histograma G")
plt.show()
cv2.waitKey(0)

histograma(conteoD, valD)
plt.title("Histograma D")
plt.show()
cv2.waitKey(0)

#Valores 
kernel_bajo = np.array([80,80,80], np.uint8)
kernel_alto = np.array([200,200,200], np.uint8)
kernel2_bajo = np.array([210,210,210], np.uint8)
kernel2_alto = np.array([252,252,252], np.uint8)

#Procesamiento para Golden
G_decon = cv2.inRange(Gimage,kernel_bajo,kernel_alto)
cv2.imshow('pg1',G_decon)
cv2.waitKey(0)

G_decon2 = cv2.inRange(Gimage,kernel2_bajo,kernel2_alto)
cv2.imshow('pg2',G_decon2)
cv2.waitKey(0)

kernel_totalG = cv2.add(G_decon,G_decon2)
cv2.imshow('pgt',kernel_totalG)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Procesamiento para Defective 
D_decon = cv2.inRange(Dimage, kernel_bajo, kernel_alto)
cv2.imshow('pd1',D_decon)
cv2.waitKey(0)

D_decon2 = cv2.inRange(Dimage, kernel2_bajo, kernel2_alto)
cv2.imshow('pd2',D_decon2)
cv2.waitKey(0)

kernel_totalD = cv2.add(D_decon,D_decon2)
cv2.imshow('pdt',kernel_totalD)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Operador para mascaras 
gold_P = cv2.bitwise_and (Gimage, Gimage, mask = kernel_totalG)
defect_p = cv2.bitwise_and (Dimage, Dimage, mask = kernel_totalD)

cv2.imshow('final g',gold_P)
cv2.imshow('final d',defect_p)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Resta de Defective a Gold

diff = cv2.subtract(gold_P, defect_p)
cv2.imshow('resta',diff)
cv2.waitKey(0)
cv2.destroyAllWindows()