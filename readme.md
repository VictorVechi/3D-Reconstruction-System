

<p align="center"><a href="#portuguese"><img src="https://static.todamateria.com.br/upload/ba/nd/bandeira-do-brasil-og.jpg" width="50" height="32"> <b>Português</b> </a> <a href="#english"> <img src="https://static.mundoeducacao.uol.com.br/mundoeducacao/2022/05/bandeira-estados-unidos.jpg" width="50" height="32"> <b>English</b></a></p>
<section id="portuguese">
<h1>Reconhecimento e reconstrução de objetos 3D a partir de imagens calibradas e nuvens de pontos</h1>

<p align="justify"><b>Resumo:</b> A reconstrução 3D, técnica fundada em visão computacional, envolve conceitos de física e geometria para reproduzir um objeto de forma virtual, mantendo suas características básicas (dimensões, formato e volume). Para isso, são necessários dados do objeto, cuja função é representar seus descritores, podendo ser obtidos a partir de sensores de profundidade, câmeras digitais, e outros equipamentos. Quanto maior a quantidade de dados, mais preciso é o resultado final. Os descritores são conjuntos de características que descrevem um objeto, como superfície, bordas, contorno, etc. Em sistemas de reconstrução 3D, são utilizados como base para criação da malha tridimensional. As abordagens para esse processo variam, principalmente devido à natureza dos descritores, que pode ser 2D ou 3D. Optar por uma ou outra fica em função do objetivo da aplicação. Enquanto descritores 3D possuem características físicas mais precisas, os descritores 2D permitem um mapeamento de textura com maior qualidade. Assim, este trabalho apresenta um sistema para reconstrução 3D baseado em imagens processadas e nuvens de pontos que, a partir da indicação de um conjunto de dados pelo usuário, seja capaz de recriar as características físicas, textura e cor do objeto. Ele consiste em uma abordagem específica, que utiliza descritores 2D e 3D previamente digitalizados. Além disso, o sistema proposto colabora com uma pesquisa de visão computacional desenvolvida no Instituto Federal do Paraná, que é responsável pela captura das imagens e nuvens de pontos. Para tanto, o sistema foi implementado usando a linguagem de programação Python, instalado com as bibliotecas Numpy, OpenCV-Python e PyntCloud. Utilizando o algoritmo grabcut, foi possível determinar as coordenadas do objeto em relação ao cenário. As coordenadas foram utilizadas para filtrar as nuvens de pontos e obter, de fato, os descritores do objeto. Os pontos filtrados são reorganizados como vértices e  utilizados para a criação das arestas e faces. A reconstrução do objeto é feita a partir da junção de todos os dados processados, que são exportados para um arquivo 3D. O procedimento experimental resultou em 33% dos objetos reconstruídos apresentando as características físicas do objeto original com poucas deformações e sendo identificáveis. A combinação de descritores 2D e 3D reduziu a necessidade de utilizar algoritmos complexos para a reconstrução dos objetos em dimensões reais e permitiu que fosse feito o mapeamento de textura. A desvantagem deste método, no entanto, é a grande quantidade de dados para serem processados, o que resultou em distorções no objeto final. Embora os resultados obtidos não apresentem qualidade elevada, o sistema se mostrou promissor ao interpretar os diferentes descritores para a reconstrução de forma eficiente, realizando todo o processo em menos de dois minutos. Os objetos reconstruídos estão inclusos no trabalho.</p>

<b>Palavras-chave:</b> Reconstrução 3D; Visão computacional; Malha tridimensional; Nuvem de pontos; Mapeamento de textura.<br>

**Objetivos**

- [x] Extrair a localização do objeto a partir de uma imagem.
- [x] Utilizar a localização para filtrar os pontos de interesse dentro da nuvem
- [x] Utilizar as imagens para criar um mapa de textura do objeto
- [x] Utilizar os pontos para criar a malha 3D
- [x] Adicionar textura à malha formando o objeto final.
- [x] Salvar o objeto como um arquivo 3D.

# Funcionamento

A princípio, o sistema recebe uma pasta (que deve ser criada manualmente) que contenha os arquivos de imagem e nuvem de pontos necessários para a reconstrução. Com esses arquivos, ele deve realizar sozinho a tarefa de interpretar as informações recebidas e utilizá-las para recriar um objeto 3D. 

# Requisitos

<ul>
  <li>Python 3.10.4</li>
  <li>OpenCV-Python 4.6.0</li>
  <li>PyntCloud 0.3.1</li>
  <li>Numpy 1.23.1</li>
  <li>PyQt6 6.4.0</li>
  <li>Easygui 0.98.3</li>
  <li>Dataset de imagens</li>
  <li>Dataset de nuvens de pontos</li>
</ul>

# Resultados

<ol type='a'>
  <li>Reconstrução parcial completa</li>
  <li>Reconstrução parcial da malha com textura insatisfatória</li>
  <li>Reconstrução parcial da textura com malha insatisfatória</li>
  <li>Reconstrução insatisfatória</li>
</ol>

![Objetos](https://user-images.githubusercontent.com/53799801/206076019-c7c85fa3-336d-4698-a357-6cea9f93b73b.png)
</section>

<section id="english">
<h1>3D reconstruction based on processed images and point clouds</h1>

<p align="justify"><b>Abstract:</b> 3D reconstruction, a technique based on computer vision, involves concepts of physics and geometry to virtually reproduce an object, maintaining its basic features (dimensions, shape, and volume). To achieve this, object data is needed, whose function is to represent its features, which can be obtained from depth sensors, digital cameras, and other equipment. The greater the amount of data, the more accurate the final result. Features are sets of data that describe an object, such as surface, edges, contour, etc. In 3D reconstruction systems, they are used as a basis for the three-dimensional mesh. There are different approaches to obtain it, mainly due to the nature of the features, which can be 2D or 3D. Choosing one or another depends on the purpose of the application. While 3D features are physically more accurate, 2D features allow higher quality texture mapping. Hence, this work presents a system for 3D reconstruction based on processed images and point clouds that, from a set of data given by the user, is capable of recreating the physical features, texture, and color of the object. It consists of a specific approach, which uses previously digitized 2D and 3D features. In addition, the proposed system collaborates with a computer vision research developed at the Federal Institute of Paraná, which is responsible for capturing images and point clouds. Therefore, the system was developed using Python, installed with Numpy, OpenCV-Python, and PyntCloud libraries. Using the grabcut algorithm, it was possible to determine the coordinates of the object in relation to the scenario. The coordinates were used to filter the point clouds and obtain the actual object features. The filtered points are rearranged as vertices and used for creating edges and faces. The reconstruction of the object is done by joining all the processed data, which are exported to a 3D file. The experimental procedure resulted in 33% of the reconstructed objects having the physical features of the original object with little deformation and being recognizable. The combination of 2D and 3D descriptors reduced the need to use complex algorithms to reconstruct objects in real dimensions and allowed texture mapping to be performed. The disadvantage of this method, however, is the large amount of data to be processed, which resulted in distortions in the final object. Although the results obtained do not show high quality, the system showed promise in interpreting the different features for the reconstruction efficiently, performing the entire process in less than two minutes. The reconstructed objects are included in this paper.</p>

<b>Keywords:</b> 3D Reconstruction; Computer vision; tridimensional mesh; pointcloud; texture mapping.<br>

**Objectives**

- [x] Extract object position from an image.
- [x] Use the position to filter points of interest within the cloud.
- [x] Use the images to create an object texture map.
- [x] Using the points to create the 3D mesh.
- [x] Add texture to the mesh forming the final object.
- [x] Save the object as a 3D file.

# How it works

At first, the system receives a folder (which must be created manually) that contains the necessary image and point cloud files for the reconstruction. With these files, he must carry out the task of interpreting the information received and using it to recreate a 3D object.

# Requirements

<ul>
  <li>Python 3.10.4</li>
  <li>OpenCV-Python 4.6.0</li>
  <li>PyntCloud 0.3.1</li>
  <li>Numpy 1.23.1</li>
  <li>PyQt6 6.4.0</li>
  <li>Easygui 0.98.3</li>
  <li>Dataset de imagens</li>
  <li>Dataset de nuvens de pontos</li>
</ul>

# Result Samples

<ol type='a'>
  <li>Complete partial reconstruction</li>
  <li>Partial reconstruction of the mesh with unsatisfactory texture</li>
  <li>Partial texture reconstruction with unsatisfactory mesh</li>
  <li>Unsatisfactory reconstruction</li>
</ol>

![Objetos](https://user-images.githubusercontent.com/53799801/206076019-c7c85fa3-336d-4698-a357-6cea9f93b73b.png)
</section>

<!-- contributors -->
<!-- /contributors -->

---
#### &copy; Leonardo Salgado & Victor Vechi
