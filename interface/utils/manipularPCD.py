import numpy as np
import utils.calculos as calc
from pyntcloud import PyntCloud as pcd

CONST_MaiorZ = 0.813000047
CONST_MenorZ = 0.759000041

def filterValues(x1, y1, x2, y2):
    menorx = ((x1/7.391630)/100)+(-0.375560)
    maiorx = ((x2/7.391630)/100)+(-0.375560)
    menory = ((y1/7.391630)/100)+(-0.349560)
    maiory = ((y2/7.391630)/100)+(-0.379560)
    return maiorx, menorx, maiory, menory

def getPoints(file, name, descritores):
    path = name+"/"+file

    file = file.split(".")
    file = file[0].split("_")
    file = file[1]
    for i in descritores:
        name = i['img'].split(".")
        name = name[0].split("_")
        name = name[2]
        if name == file:
            x = i['x']
            y = i['y']
            w = i['w']
            h = i['h']
    maiorx, menorx, maiory, menory = filterValues(x, y, x + w ,y + h)

    cloud = pcd.from_file(path)
    pontos = np.array(cloud.points)
    vertices = []
    for i in pontos[::25, :]:
        if i[0] > maiorx or i[0] < menorx or i[1] > maiory or i[1] < menory or i[2] < CONST_MenorZ or i[2] > CONST_MaiorZ:
            continue
        else:
            vertices.append(i)
            
    return vertices, int(file)

def corrigeOrientacao(vertices):
    mediaLocal = []
    n_pontos = []
    for pontos in vertices:
        sumX = 0
        sumY = 0
        sumZ = 0
        media = {}
        for i in pontos["pontos"]:
            sumX += i[0]
            sumY += i[1]
            sumZ += i[2]
        midpointX = sumX/len(pontos["pontos"])
        midpointY = sumY/len(pontos["pontos"])
        midpointZ = sumZ/len(pontos["pontos"])
        media["x"] = midpointX
        media["y"] = midpointY
        media["z"] = midpointZ
        pontos["pontos"] = calc.rotateY(midpointY, midpointZ, pontos["pontos"])
        n_pontos.append(pontos["pontos"])
        mediaLocal.append(media)
    mediaX = (mediaLocal[0]["x"]+mediaLocal[2]["x"])/2
    mediaY = (mediaLocal[0]["y"]+mediaLocal[1]["y"]+mediaLocal[2]["y"]+mediaLocal[3]["y"])/4
    mediaZ = ((mediaLocal[0]["z"]+mediaLocal[2]["z"])/2) + ((mediaLocal[3]["x"]+mediaLocal[1]["x"])/2)
    mediaGeral = [mediaX, mediaY, mediaZ]
    n_vertices = calc.rotateX(mediaLocal, mediaGeral, n_pontos)
    return n_vertices
