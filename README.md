o # poly_class: manipulação de polinômios

Um script em Python, com o uso das bibliotecas padrão json e pathlib, para manipulação de polinômios de qualquer grau por meio da criação de uma classe. Permite avaliar o valor num ponto específico, realizar integração e derivação simbólicas, calcular a integral definida em um intervalo, obter raízes utilizando os métodos de Newton e da bisseção e ler e salvar dicionários em arquivos json para representação dos polinômios.

# Como importar a classe

```Python
from poly import Polynomial
```

E utilize a classe Polynomial normalmente no seu script.

# Diretórios utilizados

A pasta poly_class consiste em, além do gitignore e do readme, duas pastas: src e data.

## src

Nela, encontram-se os scripts poly.py e main.py.

### poly.py

Onde se encontra a classe juntamente com seus métodos para uso.

### main.py

Exemplifica e demonstra o uso de todos os métodos.

## data

A pasta data é criada pelo script poly.py (usando o módulo pathlib) caso o usuário utilize o método de salvar um dicionário em arquivo json e a pasta já não exista.
Nela, são armazenados os arquivos json para ler e salvar na manipulação de polinômios.

## Como utilizar os métodos

* `__init__ (self, coef_at_degree={}) `: cria uma instância da classe Polynomial tomando por parâmetro coef_at_degree, dicionário cujas chaves são inteiros não negativos representando os graus e cujos valores são números (int ou float) representando os coeficientes correspondentes a esses graus. O padrão para o dicionário é um dicionário vazio, criando um polinômio nulo.
* `eval (self, x)`: toma por parâmetro um número (int ou float) x e avalia o polinômio nesse ponto x, retornando o valor obtido.
* `symbolic_integrate (self, constant=0)`: retorna a integral simbólica do polinômio. O parâmetro opcional constant recebe um número (int ou float) que define o valor do coeficiente no grau 0, sendo 0 o valor padrão.
* `interval_integrate (self, interval)`:
