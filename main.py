import buscarArquivo as search
import tratarImgs as img2
import mapaTextura as texture
#import manipularPCD as pcd

name = input("Insira o nome da pasta (Obs: O nome também será usado para nomear o arquivo):\n")
imgs, pcd = search.search(name)
descritores = []
for file in imgs:
    img, f_img, aux_img = img2.getImgs(name, file)
    x, y, w, h, aux_img = img2.getContours(img, aux_img)
    dicto = {'img': file, 'x': x, 'y': y, 'w': w, 'h': h}
    descritores.append(dicto)
    print(len(descritores), "de", len(imgs))

texture.mapping(descritores, name)
