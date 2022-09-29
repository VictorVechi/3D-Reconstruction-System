import buscarArquivo as search
import tratarImgs as img2
import mapaTextura as texture
import manipularPCD as features

#Inicia o programa pedindo o nome da pasta, que é buscado nos arquivos com a classe search
name = input("Insira o nome da pasta (Obs: O nome também será usado para nomear o arquivo):\n")
#Única função da classe, busca arquivos dentro da pasta com o nome indicado
imgs, pcd = search.search(name)
descritores = []

print("Tratando imagens")
for file in imgs:
    img, f_img, aux_img = img2.getImgs(name, file)
    x, y, w, h, aux_img = img2.getContours(img, aux_img)
    dicto = {'img': file, 'x': x, 'y': y, 'w': w, 'h': h}
    descritores.append(dicto)
print("!!...")

texture.mapping(descritores, name)

def reordena(n):
    idx = n["ang"]	
    return idx

print("Manipulando pcd")
vertices = []
for file in pcd:
    pontos, idx = features.getPoints(file, name, descritores)
    dicto = {"ang": idx, "pontos": pontos}
    vertices.append(dicto)

vertices.sort(key = reordena)

f_vertices = features.corrigeOrientacao(vertices)
print("!!!!.")


features.createObj(f_vertices, name)
