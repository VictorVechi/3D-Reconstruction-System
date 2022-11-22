# Reconhecimento e reconstrução de objetos 3D a partir de imagens calibradas e nuvens de pontos

Repositório dedicado ao projeto de TCC desenvolvido para o curso técnico de informática do IFPR, usaremos ele para poder salvar arquivos seguindo uma linha cronológica para ficar organizado.

<p align="justify"><b>Resumo:</b> A reconstrução 3D, técnica fundada em visão computacional, envolve conceitos de física e geometria para reproduzir um objeto de forma virtual, mantendo suas características básicas (dimensões, formato e volume). Para isso, são necessários dados do objeto, cuja função é representar seus descritores, que podem ser obtidos a partir de sensores de profundidade, câmeras digitais, e outros equipamentos. Quanto maior a quantidade de dados, mais preciso é o resultado final. Os descritores são conjuntos de características que descrevem um objeto, como superfície, bordas, contorno, etc. Em sistemas de reconstrução 3D, são utilizados como base para criação da malha tridimensional. As abordagens para esse processo variam, principalmente devido à natureza dos descritores, que pode ser 2D ou 3D. Optar por uma ou outra fica em função do objetivo da aplicação. Enquanto descritores 3D possuem características físicas mais precisas, os descritores 2D permitem um mapeamento de textura com maior qualidade. Assim, este trabalho apresenta um sistema para reconstrução 3D baseado em imagens processadas e nuvens de pontos, independente de qualquer auxílio do usuário, capaz de recriar as características físicas, textura, e cor do objeto com qualidade. Ele consiste em uma abordagem específica, que utiliza descritores 2D e 3D. Além disso, o sistema proposto colabora com uma pesquisa de visão computacional desenvolvida no Instituto Federal do Paraná, que é responsável pela captura das imagens e nuvens de pontos. Para tanto, o sistema foi implementado usando a linguagem de programação <i>Python</i>, instalado com as bibliotecas <i>Numpy</i>, <i>OpenCV-Python</i> e <i>PyntCloud</i>. Até o momento, o sistema utiliza as imagens para criar um mapa de textura e determinar a posição do objeto na cena, possibilitando filtrar os descritores dentro da nuvem de pontos. Com isso, espera-se que a partir dos pontos obtidos seja possível criar a malha tridimensional e aplicar a ela o mapa de textura, finalizando o objeto.</p>

<b>Palavras-chave:</b> Reconstrução 3D. Visão computacional. <i>OpenCV-Python</i>. Nuvem de pontos. Mapeamento de textura. <br>

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
