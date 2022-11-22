import cv2
import os
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

def reordena(n):
    idx = n["ang"]	
    return idx

def mapping(descritores, pasta):
    angulos = []
    cima = []
    baixo = []
    print("Criando mapa de textura")
    for i in descritores:
        angle = i['img'].split(".")
        angle = angle[0].split("_")
        angle = angle[2]

        path = "dataset/"+pasta+"/"+i['img']
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        imgCropped = img[i['y']: i['y'] + i['h'], i['x']: i['x'] + i['w']]
        angulos.append({"ang": int(angle), "img": imgCropped})
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

    angulos.sort(key = reordena)
    #map = ([angulos[0]["img"], angulos[1]["img"], angulos[2]["img"], angulos[3]["img"]], [corCima, corCima, corBaixo, corBaixo])
    map = ([corCima, corCima, corBaixo, corBaixo], [angulos[0]["img"], angulos[1]["img"], angulos[2]["img"], angulos[3]["img"]])
    stackedImages = stackImages(2,map)

    newPath = f"obj/{pasta}/{pasta}_textura.png"
    caminho = os.path.exists(f"obj/{pasta}")
    if caminho == False:
        os.mkdir(f"obj/{pasta}")
    cv2.imwrite(newPath, stackedImages)
    writeMTL(pasta)
    
    print("!!!....")

def apply(vertices, descritores):
    print("Aplicando textura na malha")
    textureMap = []
    for pontos in vertices:
        angValue = 0
        for i in descritores:
            name = i['img'].split(".")
            name = name[0].split("_")
            name = name[2]
            if int(name) == pontos["ang"]:
                x = i['x']
                y = i['y']
                w = i['w']
                h = i['h']
        for i in pontos["pontos"]:
            #u é horizontal e v é vertical
            u = int(((i[0]-(-0.375560))*100)*(7.391630))-x
            v = int(((i[1]-(-0.375560))*100)*(7.391630))-y
            if u < 0: u+= w
            if v < 0: v+= h
            if u > w: u = w
            if v > h: v = h
            vt = [((u/w)/4)+angValue, (v/h)/2]
            textureMap.append(vt)
        angValue += 0.25
    print("!!!!!!.")
    return textureMap

def writeMTL(name):
    file = "obj/"+name+"/"+name+".mtl"
    meshfile = open(file, "w")
    meshfile.write("# Arquivo de textura MTL\n")
    meshfile.write("# Projeto realizado pelo IFPR - Campus Pinhais\n")
    meshfile.write("# Material Count: 1\n\n")
    meshfile.write(f"newmtl {name}_textura\n")
    meshfile.write("Ns 225.000000\n")
    meshfile.write("Ka 1.000000 1.000000 1.000000\n")
    meshfile.write("Kd 0.800000 0.800000 0.800000\n")
    meshfile.write("Ks 0.500000 0.500000 0.500000\n")
    meshfile.write("Ke 0.000000 0.000000 0.000000\n")
    meshfile.write("Ni 1.450000\n")
    meshfile.write("d 1.000000\n")
    meshfile.write("illum 2\n")
    meshfile.write(f"map_Kd {name}_textura.png")

