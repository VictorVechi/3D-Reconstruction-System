import time
from collections import defaultdict
import numpy as np
import math

def distanceBetween(p1, p2):
    distancia = math.sqrt(math.pow(p2[0]-p1[0], 2)+math.pow(p2[1]-p1[1], 2)+math.pow(p2[2]-p1[2], 2))
    return distancia

def createMesh(vertices):
    print("Gerando malha tridimensional")
    arestas = []
    vertex_numbers = []
    radius = 0.0235
    vertices = np.array(vertices)
    for v in range(len(vertices)):
        vertex_numbers.append(v+1)
        vertice = vertices[v]
        distance = lambda a: np.power(np.subtract(a, vertice), 2)
        
        #Filtra os pontos dentro do raio máximo
        nearPoints = np.where(distance(vertices) <= radius**2)
        nearestPoints, frequency = np.unique(nearPoints[0], return_counts=True)
        intheArea = np.where(frequency == 3)
        
        #Escreve as arestas
        for p in intheArea[0]:
            try:
                edge = [v+1, nearestPoints[p]+1]
            except IndexError:
                break
            distancia = distanceBetween(vertices[v], vertices[nearestPoints[p]])
            if edge in arestas or [edge[1], edge[0]] in arestas:
                continue
            elif v+1 == p+1:
               continue
            elif distancia < 0.005:
                continue
            else:
               arestas.append(edge)
    
    #cria as faces
    edge_lookup = defaultdict(set)
    for a, b in arestas:
        edge_lookup[a] |= {b}
        edge_lookup[b] |= {a}

    faces = set()
    for a in vertex_numbers:
        for b in edge_lookup[a]:
            for c in edge_lookup[a]:
                if b in edge_lookup[c]:
                    faces.add(frozenset([a, b, c]))
    toRemove = []
    toAdd = []
    n_faces = []
    for f in faces:
        if len(f) < 3:
            toRemove.append(f)
        else: 
            toAdd.append(list(f))

    for x in toRemove:
        faces.remove(x)
    for a in toAdd:
        n_faces.append(a)
    print("!!!!!..")
    return arestas, n_faces

def timeElapsed(start):
    now = time.time()
    tempo = now - start
    return tempo

def writeOBJ(vertices, arestas, faces, texture, name, start):
    print("Escrevendo o objeto")
    time = timeElapsed(start)

    path = "obj/"+name+"/"+name+".obj"
    meshfile = open(path, "w")
    meshfile.write("# Esse arquivo OBJ foi reconstruido por Leonardo e Victor\n")
    meshfile.write("# Projeto realizado pelo IFPR - Campus Pinhais\n")
    meshfile.write(f"# Tempo empregado: {time: .2f} segundos\n")
    meshfile.write(f"# Vertices: {len(vertices)}\n")
    meshfile.write(f"# Arestas: {len(arestas)}\n")
    meshfile.write(f"# Faces: {len(faces)}\n\n")

    meshfile.write(f"mtllib {name}.mtl\n")
    for v in vertices:
        meshfile.write(f"v {v[0]} {v[1]} {v[2]}\n")
    #meshfile.write("vt 1.000000 1.000000\n")
    #meshfile.write("vt 0.0000 0.0010\n")
    #meshfile.write("vt 0.0050 1.0000\n")
    for vt in texture:
        meshfile.write(f"vt {vt[0]: .6f} {vt[1]: .6f}\n")
    meshfile.write(f"usemtl {name}_textura\n")
    for f in faces:
        meshfile.write(f"f {f[0]}/{f[0]} {f[1]}/{f[1]} {f[2]}/{f[2]}\n")
    meshfile.close()
    print("!!!!!!!")