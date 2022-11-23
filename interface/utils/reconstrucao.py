import time
import utils.buscarArquivo as search
import utils.tratarImgs as image
import utils.mapaTextura as texture
import utils.manipularPCD as features
import utils.malha as mesh

#Inicia o programa pedindo o nome da pasta, que é buscado nos arquivos com a classe search
def exec(path,name):
    #Registra o tempo de início da reconstrução, para calcular o tempo empregado
    start = time.time()
    #Única função da classe, busca arquivos dentro da pasta com o nome indicado
    imgs, pcd = search.search(path)

    #Tratamento das imagens 2D
    print("Tratando imagens")
    descritores = []
    for file in imgs:
        img, f_img, aux_img = image.getImgs(path, file)
        #Retorna as coordenadas do objeto na imagem
        x, y, w, h, aux_img = image.getContours(img, aux_img)
        dicto = {'img': file, 'x': x, 'y': y, 'w': w, 'h': h}
        descritores.append(dicto)
    print("!!....")

    #Mapeamento de textura
    texture.mapping(descritores, path, name)

    #Tratamento das nuvens de pontos
    print("Organizando nuvem de pontos")
    vertices = []
    for file in pcd:
        #Utiliza as coordenadas obtidas da imagem para localizar o objeto na nuvem
        pontos, idx = features.getPoints(file, path, descritores)
        dicto = {"ang": idx, "pontos": pontos}
        vertices.append(dicto)

    #Reordena os ângulos do objeto
    def reordena(n):
        idx = n["ang"]	
        return idx

    vertices.sort(key = reordena)

    #Faz a junção dos ângulos do objeto para formar seu contorno
    f_vertices = features.corrigeOrientacao(vertices)
    print("!!!!..")

    #Faz associação dos pontos para criação das faces
    arestas, faces = mesh.createMesh(f_vertices)

    #Faz aplicação do mapa de textura na malha
    textureMap = texture.apply(vertices, descritores)

    #Escreve o novo objeto em um arquivo
    mesh.writeOBJ(f_vertices, arestas, faces, textureMap, name, start)

    print("Finalizado")