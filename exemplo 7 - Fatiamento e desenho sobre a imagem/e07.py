import cv2
image = cv2.imread('img/saida.jpg')

yini=int(input('informe o pixel de inicio na altura:'))
yfim=int(input('informe o pixel de fim na altura:'))
xini=int(input('informe o pixel de inicio na largura:'))
xfim=int(input('informe o pixel de fim na largura:'))
image[yini:yfim,xini:xfim] = (255,0,0)
cv2.imshow("Imagem alterada: ",image)
cv2.waitKey(0)
