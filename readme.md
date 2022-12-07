# Reconhecimento e reconstrução de objetos 3D a partir de imagens calibradas e nuvens de pontos

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
