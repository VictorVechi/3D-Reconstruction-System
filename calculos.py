import math


def rotateY(midpointY, midPointZ, pontos):
    angulo = math.radians(100)
    seno = math.sin(angulo)
    cosseno = math.cos(angulo)

    if cosseno == 6.123233995736766e-17:
        cosseno = 0

    if seno == 6.123233995736766e-17:
        seno = 0

    for i in pontos:
        coordY = i[1]-midpointY
        coordX = i[2]-midPointZ
        i[1] = (coordX*cosseno - coordY*seno)+midpointY
        i[2] = (coordX*seno + coordY*cosseno)+midPointZ

    return pontos

