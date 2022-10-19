import cv2
import numpy as np

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

def mapping(descritores, pasta):
    angulos = []
    cima = []
    baixo = []
    print("Obtendo mapa de textura")
    for i in descritores:
        path = "dataset/"+pasta+"/"+i['img']
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        imgCropped = img[i['y']: i['y'] + i['h'], i['x']: i['x'] + i['w']]
        angulos.append(imgCropped)
        b, g, r = imgCropped[5, i['w']//2]
        cima.append([r, g, b])
        b, g, r = imgCropped[i['h']-1, i['w']//2]
        baixo.append([r, g, b])

    r, g, b = 0, 0, 0
    for color in cima:
        r += color[0]
        g += color[1]
        b += color[2]
    corCima = np.zeros((480, 240, 3), np.uint8)
    corCima[:] = b//4, g//4, r//4
    
    r, g, b = 0, 0, 0
    for color in baixo:
        r += color[0]
        g += color[1]
        b += color[2]
    corBaixo = np.zeros((512, 240, 3), np.uint8)
    corBaixo[:] = b//4, g//4, r//4

    map = ([angulos[0], angulos[1], angulos[2], angulos[3]], [corCima, corCima, corBaixo, corBaixo])
    stackedImages = stackImages(2,map)

    newPath = "dataset/"+pasta+"/"+pasta+"_textura.png"
    cv2.imwrite(newPath, stackedImages)
    print("!!!...")
