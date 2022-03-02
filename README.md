# puzzle8-IA
## :warning: Introdução
<p align="justify">O puzzle 8 consiste em um jogo de tabuleiro 3 x 3 com oito peças numeradas de 1 a 8 e uma posição vazia que pode ser trocada com qualquer peça ao seu redor nas direções cima, baixo, esquerda e direita, respeitando os limites de linha e coluna do tabuleiro.
O tabuleiro possui uma configuração objetivo a ser atingida e inicia-se em uma configuração aleatória, tendo o jogador que movimentar suas peças afim de alcançar a condição objetivo. <br><br>Abaixo é possível visualizar um exemplo de configuração inicial e objetivo a ser atingido através de movimentação das peças</p><br>

<p align="center">
<img width="400" height="400" src="https://www.datasciencecentral.com/wp-content/uploads/2021/10/sol05.gif"/><br>
Figura 1 - Puzzle8 <br>Fonte: <a href="https://www.datasciencecentral.com/using-uninformed-informed-search-algorithms-to-solve-8-puzzle-n/">Data Science Central</a>
</p>

## :pencil2: Resolução
<p align="justify">O algoritmo desenvolvido para solução do problema foi implementado na linguagem Python e utiliza dois métodos de busca para o estado objetivo, sendo eles:</p>

### :heavy_check_mark: Busca em largura 
<p align="justify">Selecionado como método "cego", tenta uma resolução por força bruta ao expandir a árvore de possíveis jogadas sem verificar o impacto na proximidade com a solução do problema. Nessa abordagem, a configuração inicial do tabuleiro a ser resolvido influencia diretamente na quantidade de nós expandidos na árvore e no custo computacional para finalização do jogo</p>
<p align="center">
<img width="600" height="400" src="https://player.slideplayer.com/16/4929511/data/images/img4.jpg"><br>
Figura 2 - Busca em largura<br>Fonte: <a href="https://slideplayer.com/slide/4929511/">Clique aqui</a></p>

### :heavy_check_mark: Distância Manhattan
<p align="justify"> Selecionado como um método heurístico, verifica a distância da posição atual de cada peça com suas respectivas posições objetivo, e procura retornar uma solução com o menor número de jogadas possíveis ao expandir os nós de menor distância na árvore gerada. Nessa abordagem, uma quantidade considerável de configurações dos nós da árvore é descartada ao se verificar sua distância com o estado objetivo. </p>
<p align="center">
<img width="600" height="400" src="https://images.slideplayer.com/35/10342447/slides/slide_30.jpg"><br>
Figura 3 - Distância Manhattan <br>Fonte: <a href="https://ros.cheapsalesstore.ru/content?c=8%20puzzle%20hill%20climbing&id=16">Clique aqui</a></p>

<br><p align="justify">Com isso, o algoritmo recebe uma configuração inicial do jogo e a armazena como estado objetivo a ser atingido, embaralha arbitrariamente as peças e busca a partir do estado pós embaralhamento o estado inicial através das duas métricas citadas acima. </p>

## :video_game: Executando o código
<p align="justify">Clone o repositório em sua máquina com o seguinte comando:</p>

```console
$ git clone https://github.com/LuizFelipe-5/puzzle8-IA.git
```

<p> Abra no terminal o diretório onde se encontra o arquivo puzzleSimulator.py e execute o seguinte comando:</p>

```console
$ python puzzleSimulator.py
```
  
