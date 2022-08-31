import cv2
import numpy as np
import openCv as cvL
import pymeshlab as pml

path = "imagens/schin.jpg"
f_img = cv2.imread(path, cv2.IMREAD_COLOR)
f_img = cv2.resize(f_img, (640, 480))
aux_img = f_img.copy()
aux_img[121:373, 220:420] = 255 - aux_img[121:373, 220:420]

bounding_box = [220, 121, 420-220, 373-121] 
seg = np.zeros(f_img.shape[:2],np.uint8)
x,y,width,height = [220, 121, 420-220, 373-121]
cv2.rectangle(aux_img, (x, y), (x + width, y + height), (0, 255, 255), 1)
seg[y:y+height, x:x+width] = 1
background_mdl = np.zeros((1,65), np.float64)
foreground_mdl = np.zeros((1,65), np.float64)

cv2.grabCut(f_img, seg, bounding_box, background_mdl, foreground_mdl, 5, cv2.GC_INIT_WITH_RECT)

mask_new = np.where((seg==2)|(seg==0),0,1).astype('uint8')
#cv2.imshow('Mask', mask_new)

img = f_img*mask_new[:,:,np.newaxis]
#cv2.imshow('Output', img)

# remonta a imagem invertida
img_fundo = f_img.copy()
img_fundo = 255
new_img = np.where(img!=0, img_fundo, img)
new_img = ~new_img
#cv2.imshow("Teste", new_img)

# converte a imagen para niveis de cinza
normal = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

# dilata a imagem para remover os ruidos e ter a posição exata do objeto
kernel = np.ones((3,3), np.uint8)
dilate = cv2.dilate(normal, kernel, iterations=1)
#cv2.imshow('Dilate', dilate)

contours, hierarchy = cv2.findContours(~dilate, cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)

max_area = -1
for c in range(len(contours)):
    area = cv2.contourArea(contours[c])
    if area>max_area:
        cnt = contours[c]
        max_area = area

x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(aux_img, (x, y), (x + w, y + h), (0, 0, 255), 1)
#cv2.imshow('Final', aux_img)

imgCropped = f_img[y: y + h, x: x + w]
#cv2.imshow("Imagem cortada", imgCropped)
imgResult = np.zeros((480, 640, 3), np.uint8)
imgResult[y: y + h, x: x + w] = imgCropped
cv2.imshow("Resultado", imgResult)

imgStack = cvL.stackImages(0.75,([f_img, new_img], [aux_img, imgResult]))
cv2.imshow("Saida", imgStack)
cv2.waitKey(0)