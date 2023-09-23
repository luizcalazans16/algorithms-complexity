# Implementação de Tabelas de Hash (HashSet)

Este é um exemplo de implementação de um conjunto em Kotlin usando tabelas de hash (HashMap).

### Funções do Conjunto

- `add(element: T)`: Adiciona um elemento ao conjunto. Se o elemento já estiver no conjunto, ele não será duplicado.

- `remove(element: T)`: Remove um elemento do conjunto, se ele estiver presente.

- `contains(element: T)`: Verifica se um elemento está presente no conjunto e retorna verdadeiro (true) se estiver, ou falso (false) caso contrário.

- `union(otherSet: HashSet<T>): HashSet<T>`: Retorna um novo conjunto que é a união do conjunto atual com outro conjunto (`otherSet`).

- `intersection(otherSet: HashSet<T>): HashSet<T>`: Retorna um novo conjunto que é a interseção do conjunto atual com outro conjunto (`otherSet`).

- `difference(otherSet: HashSet<T>): HashSet<T>`: Retorna um novo conjunto que é a diferença entre o conjunto atual e outro conjunto (`otherSet`).

### Justificativa

A escolha de utilizar tabelas de hash (HashMap) para implementar este conjunto foi feita por diversas razões:

1. **Eficiência**: Tabelas de hash oferecem inserção, remoção e consulta eficientes em média, com complexidade de tempo média de O(1) para essas operações. Isso é importante para garantir um desempenho rápido, especialmente em conjuntos grandes.

2. **Facilidade de Implementação**: As operações de conjunto são implementadas de forma direta e eficiente, aproveitando a estrutura interna de hash para otimizar a busca e a inserção de elementos.

3. **Lidar com Colisões**: As tabelas de hash lidam bem com colisões usando encadeamento (chaining), o que significa que mesmo se dois elementos tiverem o mesmo valor de hash, eles podem ser armazenados de forma eficiente na mesma posição da tabela.

4. **Flexibilidade**: As tabelas de hash são flexíveis e podem ser usadas para implementar conjuntos de qualquer tipo de elemento.

No entanto, é importante lembrar que, em casos extremos, as colisões podem afetar o desempenho, mas a implementação padrão do Kotlin lida bem com colisões usando encadeamento. Esta implementação é adequada para conjuntos de tamanho moderado a grande, onde a eficiência na consulta e manipulação de elementos é crítica.
