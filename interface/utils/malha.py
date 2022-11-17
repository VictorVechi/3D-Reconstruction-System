import time
import numpy as np
import os

def createMesh(vertices):
    print("Gerando malha tridimensional\n")
    faces = []
    vertices = np.array(vertices)
    #O conceito de ball-pivoting é um saco
    #Eu prefiro achar outro jeito

    print("!!!!!.")
    return faces

def timeElapsed(start):
    now = time.time()
    tempo = now - start
    return tempo

def writeOBJ(vertices, faces, name, start):
    print("Escrevendo o objeto")
    time = timeElapsed(start)
    
    #print("Current working directory: {0}".format(os.getcwd()))

    pasta = "obj/"+name+".obj"
    meshfile = open(pasta, "w")
    meshfile.write("# Esse arquivo OBJ foi reconstruído por Leonardo e Victor\n")
    meshfile.write("# Projeto realizado pelo IFPR - Campus Pinhais\n")
    meshfile.write(f"# Tempo empregado: {time} segundos\n\n")
    for i in vertices:
        meshfile.write(f"v {i[0]} {i[1]} {i[2]}\n")
    for a in faces:
        meshfile.write(f"f {a[0]} {a[1]} {a[2]}\n")
    meshfile.close()
    print("!!!!!!")
