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

def correcaoPosition(pontos, bordas):
    vertices = []
    for face in pontos:
        idx = pontos.index(face)
        diff_maiorX = bordas[idx]["maiorX"]-bordas[idx-1]["maiorX"]
        diff_maiorY = bordas[idx]["maiorY"]-bordas[idx-1]["maiorY"]
        diff_maiorZ = bordas[idx]["maiorZ"]-bordas[idx-1]["maiorZ"]
        diff_menorX = bordas[idx]["menorX"]-bordas[idx-1]["menorX"]
        diff_menorZ = bordas[idx]["menorZ"]-bordas[idx-1]["menorZ"]
        if idx == 0:
            bordas[idx]["menorX"] -= diff_menorX
            bordas[idx]["maiorX"] -= diff_menorX
            bordas[idx]["maiorY"] -= diff_maiorY
            bordas[idx]["menorZ"] -= diff_menorZ
            for i in face:
                i[0] -= diff_menorX
                i[1] -= diff_maiorY
                i[2] -= diff_menorZ
        if idx == 1:
            bordas[idx]["maiorX"] -= diff_maiorX
            bordas[idx]["maiorY"] -= diff_maiorY
            bordas[idx]["maiorZ"] -= diff_menorZ
            for i in face:
                i[0] -= diff_maiorX
                i[1] -= diff_maiorY
                i[2] -= diff_menorZ
        if idx == 2:
            bordas[idx]["maiorX"] -= diff_maiorX
            bordas[idx]["maiorY"] -= diff_maiorY
            bordas[idx]["maiorZ"] -= diff_maiorZ
            for i in face:
                i[0] -= diff_maiorX
                i[1] -= diff_maiorY
                i[2] -= diff_maiorZ
        for i in face:
            vertices.append(i)
    return vertices

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
    bordas = []
    for face in pontos:
        borda = {}
        maiorX = -1000000
        menorX = 1000000
        maiorZ = -1000000
        menorZ = 1000000
        maiorY = -100000
        menorY = 10000000
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
    #Encontra as bordas do objeto
            if i[0] > maiorX: maiorX = i[0]
            if i[1] > maiorY: maiorY = i[1]
            if i[2] > maiorZ: maiorZ = i[2]
            if i[0] < menorX: menorX = i[0]
            if i[1] < menorY: menorY = i[1]
            if i[2] < menorZ: menorZ = i[2]
        borda = {"ang": deg, "maiorX": maiorX, "maiorY": maiorY, "maiorZ": maiorZ, "menorX": menorX, "menorY": menorY, "menorZ": menorZ }
        bordas.append(borda)
        deg += 90
        idx += 1
    vertices = correcaoPosition(pontos, bordas)
    return vertices
