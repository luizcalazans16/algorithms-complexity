# Path Finder

Este programa utiliza o algoritmo A* para encontrar o caminho mais curto de um ponto inicial a um ponto final em um mapa retangular.

## Funcionamento

O algoritmo A* funciona encontrando o caminho mais curto entre um ponto de partida e um ponto de destino em um grid, considerando obstáculos e custos associados a cada movimento. Ele usa a soma do custo atual e uma estimativa do custo restante (heurística) para determinar a prioridade dos nós a serem explorados.

## Funcionalidades

- **Leitura de Mapa**: O código lê um arquivo de mapa no formato especificado, contendo a descrição do ambiente e a posição inicial do objeto.

- **Tratamento de valores no mapa**: O código trata os valores no mapa, considerando os valores inteiros e interpretando corretamente os obstáculos representados pelo valor -1.

- **Movimento no mapa**: O algoritmo permite mover o objeto apenas na horizontal e na vertical, sem custo extra para trocar o eixo de movimento.

- **Cálculo do caminho mais curto**: Usa o algoritmo A* para calcular o caminho mais curto entre a posição inicial do objeto e as coordenadas fornecidas pelo usuário.

- **Apresentação do resultado**: Ao encontrar o caminho, o código apresenta o caminho escolhido com o custo total do trajeto e as coordenadas percorridas no formato solicitado.

## Como Executar

### Requisitos

- Python 3.x

### Passos

1. **Preparação**: Certifique-se de ter o arquivo `map.txt` pronto no formato especificado.

2. **Execução**:
   - Abra um terminal na pasta onde está o arquivo `path_finder.py`.
   - Execute o comando:
     
     ```
     python path_finder.py
     ```
     
   - O programa pedirá as coordenadas do ponto de destino (x, y) para encontrar o caminho até lá no mapa.
  
## Estrutura do Mapa

O mapa é representado por um arquivo de texto no seguinte formato:

```
10 8
0 7
3 1 4 -1 -1 8 8 8 0 0
3 3 2 6 2 3 8 8 1 0
3 3 3 5 6 8 10 6 1 0
0 1 1 4 0 10 10 -1 1 0
0 1 1 4 5 0 0 -1 1 0
0 1 1 1 1 0 0 -1 1 0
0 1 1 1 1 1 10 10 3 0
0 0 0 0 0 0 10 10 10 0
```

Onde:
- A primeira linha indica a largura e altura do mapa.
- A segunda linha representa as coordenadas iniciais.
- As linhas subsequentes representam o grid do mapa, onde cada número indica o custo de atravessar essa célula. Valores negativos indicam obstáculos.

## Resultados

Após a execução, o programa mostrará o custo total do caminho encontrado e a sequência de coordenadas para percorrê-lo.

### Autores
- [@Luiz Calazans](https://github.com/luizcalazans)
- [@Maurício Salin](https://github.com/MauricioSalin)
