import cv2
import numpy as np
image = cv2.imread('img/saida.jpg')

yini=int(input('informe o pixel de inicio na altura:'))
yfim=int(input('informe o pixel de fim na altura:'))
xini=int(input('informe o pixel de inicio na largura:'))
xfim=int(input('informe o pixel de fim na largura:'))
image[yini:yfim,xini:xfim] = (255,255,255)
texto = input('informe o texto: ')

#EDITAR FONTE
fonte = cv2.FONT_HERSHEY_SIMPLEX
#cv2(elemento,texto a escrever,(pixel de inicio em y,x),fonte definida acima,2,(cor rgb),2,cv2.LINE_AA)
cv2.putText(image,texto,(yini,xini),fonte,2,(0,0,0),2,cv2.LINE_AA)

cv2.imshow("Imagem alterada: ",image)
cv2.waitKey(0)
