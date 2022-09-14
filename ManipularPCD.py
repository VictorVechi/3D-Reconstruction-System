import numpy as np
from pyntcloud import PyntCloud as pcd

cloud = pcd.from_file("pcd/Yakissoba_1.pcd")

vertices = np.array(cloud.points)

def getValues(x1, y1, x2, y2):
    menorx = ((x1/7.391630)/100)+(-0.375560)
    maiorx = ((x2/7.391630)/100)+(-0.375560)
    menory = ((y1/7.391630)/100)+(-0.345560)
    maiory = ((y2/7.391630)/100)+(-0.365560)
    return maiorx, menorx, maiory, menory

def createObj(maiorx, menorx, maiory, menory):
    meshfile = open("obj/Yakissoba_1.obj", "w")
    meshfile.write("# Reconstrução Leonardo e Victor\n")
    meshfile.write("# IFPR - Campus Pinhais\n")
    progresso = 0
    for i in vertices:
        print(f"{progresso} de {len(vertices)}")
        if i[0] > maiorx or i[0] < menorx or i[1] > maiory or i[1] < menory:
            progresso += 1
            continue
        else:
            progresso += 1
            meshfile.write(f"v {i[0]} {i[1]} {i[2]}\n")
        
    meshfile.close()
