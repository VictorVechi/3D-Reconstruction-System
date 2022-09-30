import math

def getCosSin(deg):
    angulo = math.radians(deg)
    seno = math.sin(angulo)
    cosseno = math.cos(angulo)

    if cosseno == 6.123233995736766e-17:
        cosseno = 0

    if seno == 6.123233995736766e-17:
        seno = 0

    return seno, cosseno

def rotateY(midpointY, midPointZ, pontos):

    seno, cosseno = getCosSin(100)

    for i in pontos:
        coordY = i[1]-midpointY
        coordX = i[2]-midPointZ
        i[1] = (coordX*cosseno - coordY*seno)+midpointY
        i[2] = (coordX*seno + coordY*cosseno)+midPointZ

    return pontos

def rotateX(mediaLocal, mediaGeral, pontos):
    idx = 0
    deg = 0
    vertices = []
    for face in pontos:
    #Mudar posição da média local com base na média geral
        midLocalX = mediaLocal[idx]["x"]-mediaGeral[0]
        midLocalZ = mediaLocal[idx]["z"]-mediaGeral[2]
        seno, cosseno = getCosSin(deg)
        n_midLocalX = (midLocalX*cosseno - midLocalZ*seno)+mediaGeral[0]
        n_midLocalZ = (midLocalX*seno + midLocalZ*cosseno)+mediaGeral[2]
    #Mudar posição do objeto com base na nova média local
        for i in face:
            pX = (i[0]-mediaLocal[idx]["x"])
            pZ = (i[2]-mediaLocal[idx]["z"])
    #Girar o objeto com base na média local
            i[0] = (pX*cosseno - pZ*seno)+n_midLocalX
            i[2] = (pX*seno + pZ*cosseno)+n_midLocalZ
            vertices.append(i)
        deg += 90
        idx += 1

    return vertices

