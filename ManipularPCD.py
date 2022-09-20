import numpy as np
from pyntcloud import PyntCloud as pcd

def filterPoints(index, vertices):
    if index >= 2:
        i1 = vertices[index-1]
        i2 = vertices[index-2]
        diffX = i1[0] - i2[0]
        diffY = i1[1] - i2[1]
        if diffX < 0.0002 or diffY < 0.0002:
            vertices.pop(index-1)

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

    cloud = pcd.from_file(path)
    pontos = np.array(cloud.points)
    vertices = []
    for i in pontos:
        if i[0] > maiorx or i[0] < menorx or i[1] > maiory or i[1] < menory:
            continue
        else:
            vertices.append(i)
            #A função de filtrar ainda esta estranha
            #Ele esta apagando pontos demais
            #filterPoints(len(vertices), vertices)
            
    return vertices


def createObj(vertices, file):
    file = file.split(".")
    path = "obj/"+str(file[0])+".obj"
    meshfile = open(path, "w")
    meshfile.write("# Reconstrução Leonardo e Victor\n")
    meshfile.write("# IFPR - Campus Pinhais\n")
    for i in vertices:
        meshfile.write(f"v {i[0]} {i[1]} {i[2]}\n")
        
    meshfile.close()
