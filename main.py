import buscarArquivo as search
import tratarImgs as img2
import mapaTextura as texture
import ManipularPCD as features

name = input("Insira o nome da pasta (Obs: O nome também será usado para nomear o arquivo):\n")
imgs, pcd = search.search(name)
descritores = []

print("Tratando imagens")
for file in imgs:
    img, f_img, aux_img = img2.getImgs(name, file)
    x, y, w, h, aux_img = img2.getContours(img, aux_img)
    dicto = {'img': file, 'x': x, 'y': y, 'w': w, 'h': h}
    descritores.append(dicto)
print("!!..")

texture.mapping(descritores, name)

print("Manipulando pcd")
for file in pcd:
    pontos = features.getPoints(file, name, descritores)
    features.createObj(pontos, file)
print("!!!!")
