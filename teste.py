import cv2
import numpy as np
import os

bg_img = cv2.imread("/imagens/schin.jpg")
imS = cv2.resize(bg_img, (640, 480))
#cv2.imshow("Backgroud", imS)

path = "/imagens/schin.jpg"
#path = "/home/labrobotica01/localCodePtython/img/PingoDOuro_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/CBSLaranja_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/DellValleMaca_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Melita500g_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Stella_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/DTone_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Moca_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/ChocolatedeAvela_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Closeup_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Copo_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Protex_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Royal_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Rufles_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Sococo_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/ToalhaPapel_left_1.png"
#path = "/home/labrobotica01/localCodePtython/img/Yakissoba_left_1.png"
#
# path = "/home/labrobotica01/localCodePtython/img/Yakissoba_left_1.png"

f_img = cv2.imread(path, cv2.IMREAD_COLOR)


f_img = cv2.resize(f_img, (640, 480))
aux_img = f_img.copy()
#cv2.imshow("Target",f_img)

aux_img[121:373, 220:420] = 255 - aux_img[121:373, 220:420]

bounding_box = [220, 121, 420-220, 373-121] 
seg = np.zeros(f_img.shape[:2],np.uint8)
x,y,width,height = [220, 121, 420-220, 373-121]
seg[y:y+height, x:x+width] = 1
background_mdl = np.zeros((1,65), np.float64)
foreground_mdl = np.zeros((1,65), np.float64)

cv2.grabCut(f_img, seg, bounding_box, background_mdl, foreground_mdl, 5,
    cv2.GC_INIT_WITH_RECT)

# monta a mascara com o objeto
mask_new = np.where((seg==2)|(seg==0),0,1).astype('uint8')
#cv2.imshow('Mask', mask_new)

img = f_img*mask_new[:,:,np.newaxis]
#cv2.imshow('Output', img)

# insere o fundo sobre a imagem
#fundo = np.where(img==0, imS, img)
#cv2.imshow("Join", fundo)

# remonta a imagem invertida
img_fundo = f_img.copy()
img_fundo = 255
new_img = np.where(img!=0, img_fundo, img)
new_img = ~new_img
cv2.imshow("Teste", new_img)

# converte a imagen para niveis de cinza
normal = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)

# dilata a imagem para remover os ruidos e ter a posição exata do objeto
kernel = np.ones((3,3), np.uint8)
dilate = cv2.dilate(normal, kernel, iterations=1)
#cv2.imshow('Dilate', dilate)

contours, hierarchy = cv2.findContours(~dilate, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

# find largest area contour
max_area = -1
for c in range(len(contours)):
    area = cv2.contourArea(contours[c])
    #print(area)
    if area>max_area:
        cnt = contours[c]
        max_area = area

x, y, w, h = cv2.boundingRect(cnt)
cv2.rectangle(aux_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
#cv2.imshow('Final', aux_img)

# identifica a area de interesse  
res = cv2.bitwise_and(f_img, f_img, mask=dilate)
dif = f_img-res
#cv2.imshow("Image", dif)
# extrai o objeto de intesse
img_save = dif[y:y+h, x:x+w]
#cv2.imshow("object of interest", img_save)

# paga o nome do arquivo e o caminho para gravar a imagem recortada
basename = os.path.basename(path)
path = "/temp/img_cut"
os.chdir(path)
if cv2.imwrite(basename, img_save):
    print("Saved File!!")

cv2.waitKey()
