import numpy as np 
import cv2

image = cv2.imread('img/saida.jpg')
image2=cv2.imread('img/saida.jpg')

image[100:280,200:380]=(255,0,0)
imagem3=image-image2

cv2.imshow("imagem normal",imagem3)
cv2.waitKey(0)