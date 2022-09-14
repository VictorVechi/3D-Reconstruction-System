# Reconhecimento e reconstrução de objetos 3D a partir de imagens calibradas e nuvens de pontos

Repositório dedicado ao projeto de TCC desenvolvido para o curso técnico de informática do IFPR, usaremos ele para poder salvar arquivos seguindo uma linha cronológica para ficar organizado.

- [x] Integrar o sistema ao aparelho de captura de imagens RGB e nuvem de pontos do IFPR.
- [x] Extrair a localização do objeto a partir de uma imagem.
- [x] Utilizar a localização para filtrar os pontos de interesse dentro da nuvem
- [ ] Utilizar os pontos para criar a malha 3D
- [ ] Adicionar textura à malha formando o objeto final.
- [ ] Salvar o objeto como um arquivo 3D.

# Funcionamento

A princípio, o sistema recebe uma pasta (que deve ser criada manualmente) que contenha os arquivos de imagem e nuvem de pontos necessários para a reconstrução. Com esses arquivos, ele deve realizar sozinho a tarefa de interpretar as informações recebidas e utilizá-las para recriar um objeto 3D. 

# Requisitos

<ul>
  <li>Python 3.10.4</li>
  <li>OpenCV-Python 4.6.0</li>
  <li>PyntCloud 0.3.1</li>
  <li>Numpy 1.23.1</li>
</ul>
