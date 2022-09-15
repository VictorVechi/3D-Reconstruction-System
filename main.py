import buscarArquivo as search
import tratarImgs as img2
import openCv as cvL
import cv2
#import manipularPCD as pcd

name = input("Insira o nome da pasta (Obs: O nome também será usado para nomear o arquivo):\n")
imgs, pcd = search.search(name)
for file in imgs:
    img, f_img, aux_img = img2.getImgs(name, file)
    x, y, w, h, aux_img = img2.getContours(img, aux_img)
    finalImg = img2.showResultado(f_img, x, y, w, h)

    imgStack = cvL.stackImages(0.75,([f_img, img], [aux_img, finalImg]))
    cv2.imshow("Saida", imgStack)
    cv2.waitKey(0)
