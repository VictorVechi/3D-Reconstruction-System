import cv2
import numpy as np

#Detecta formas e contornos na imagem: findContours(Imagem, método de aquisição, aproximação)
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        #Pega a area do contorno: contourArea(contorno)
        area = cv2.contourArea(i)
        print(area)
        #Desenha os contornos: drawContours(Imagem, contorno, index do contorno, cor, espessura)
        if area>200:
            cv2.drawContours(imgContour, i, -1, (172, 0, 196), 2)
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02*peri, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            #cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0,0,0), 2)
            if objCor == 4:
                cv2.putText(imgContour, "Quadrilatero",  
                        (x+(w//2)-15, y+(h//2)-15), cv2.FONT_HERSHEY_COMPLEX, 0.5,  (0,0,0), 1)
           
            
#lê a imagem
img = cv2.imread("imagens/schin.jpg")
imgContour = img.copy()
#Aplica filtro grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Aplica filtro desfocado
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
#Realça apenas os contornos
imgCanny = cv2.Canny(imgBlur, 50, 50)
#getContours(imgCanny)

#Mostra uma imagem
#cv2.imshow("Saida teste.png",img)
#cv2.imshow("Saida gray teste.png",imgGray)
#cv2.imshow("Saida blur teste.png",imgBlur)
#cv2.imshow("Saida contour teste.png",imgContour)
#cv2.waitKey(0)


#Cria uma imagem com uma matriz
#myImg = np.zeros((512, 512, 3), np.uint8)
#Retorna uma lista com altura, largura e canais
#img.shape
#Pinta um pedaço da imagem
#myImg[0:512, 0:170] = 0,0,255
#myImg[0:512, 170:340] = 0,0,127
#myImg[0:512, 340:512] = 0,0,63

#Cria uma linha: line(Imagem, ponto inicial, ponto final, cor, espessura)
#cv2.line(myImg, (0, 128), (512, 128), (255,255,255), 5)
#cv2.line(myImg, (0, 384), (512, 384), (255,255,255), 5)
#Cria um retangulo: rectangle(Imagem, ponto inicial, ponto final, cor, espessura)
#cv2.rectangle(myImg, (128, 196), (384, 324), (255,255,255), cv2.FILLED)
#Cria um círculo: circle(Imagem, ponto central, diâmetro, cor, espessura)
#cv2.circle(myImg, (85, 64), 32, (255,255,255), cv2.FILLED)
#cv2.circle(myImg, (428, 64), 32, (255,255,255), cv2.FILLED)
#cv2.circle(myImg, (85, 448), 32, (255,255,255), cv2.FILLED)
#cv2.circle(myImg, (428, 448), 32, (255,255,255), cv2.FILLED)
#Cria texto: putText(Imagem, texto, ponto inicial, fonte, escala, cor, espessura)
#cv2.putText(myImg, "Texto texto", (128, 256), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 250), 2)

#cv2.imshow("Saida teste.png",myImg)
#cv2.waitKey(0)

#Função para juntar img
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

#Chama a função de juntar imds
#imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))

#Redimensionar img
#imgResize = cv2.resize(img,(1000,500))
 
#Cortar img
#imgCropped = img[46:119,352:495]