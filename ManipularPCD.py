import numpy as np
import calculos as calc
from pyntcloud import PyntCloud as pcd

CONST_MaiorZ = 0.913000047
CONST_MenorZ = 0.719000041

def filterValues(x1, y1, x2, y2):
    menorx = ((x1/7.391630)/100)+(-0.375560)
    maiorx = ((x2/7.391630)/100)+(-0.375560)
    menory = ((y1/7.391630)/100)+(-0.345560)
    maiory = ((y2/7.391630)/100)+(-0.365560)
    return maiorx, menorx, maiory, menory

def getPoints(file, pasta, descritores):
    path = "dataset/"+pasta+"/"+file

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
    mediaX = (maiorx+menorx)/2
    mediaY = (maiory+menory)/2
    dicto = {'ang': file, "x": mediaX, "y": mediaY}

    cloud = pcd.from_file(path)
    pontos = np.array(cloud.points)
    vertices = []
    for i in pontos[::6, :]:
        if i[0] > maiorx or i[0] < menorx or i[1] > maiory or i[1] < menory or i[2] < CONST_MenorZ or i[2] > CONST_MaiorZ:
            continue
        else:
            vertices.append(i)
            
    return vertices, dicto

def rotatePoints(pontos):
    sumY = 0
    sumZ = 0
    for i in pontos:
        sumY += i[1]
        sumZ += i[2]
    midpointY = sumY/len(pontos)
    midpointZ = sumZ/len(pontos)
    pontos = calc.rotateY(midpointY, midpointZ, pontos)

    return pontos 


def createObj(vertices, file):
    file = file.split(".")
    path = "obj/"+str(file[0])+".obj"
    meshfile = open(path, "w")
    meshfile.write("# Reconstrução Leonardo e Victor\n")
    meshfile.write("# IFPR - Campus Pinhais\n")
    for i in vertices:
        meshfile.write(f"v {i[0]} {i[1]} {i[2]}\n")
        
    meshfile.close()
