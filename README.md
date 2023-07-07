# poly_class: manipulação de polinômios

Um script em Python, com o uso das bibliotecas padrão json e pathlib, para manipulação de polinômios de qualquer grau com a criação de uma classe, permitindo avaliar o valor num ponto específico, realizar integração e derivação simbólicas, calcular a integral definida em um intervalo, obter raízes utilizando os métodos de Newton e da bisseção e ler e salvar dicionários em arquivos json para representação dos polinômios.

# Como importar a classe

```Python
from poly import Polynomial
```

E utilize a classe Polynomial normalmente no seu script.

# Diretórios utilizados

A pasta poly_class consiste em, além do gitignore e do readme, duas pastas: src e data.

## src

Nela, estão os scripts poly.py e main.py.

### poly.py

Onde se encontra a classe juntamente com seus métodos para uso.

### main.py

Exemplifica e demonstra o uso de todos os métodos.

## data

A pasta data é criada pelo script poly.py (usando o módulo pathlib) caso o usuário utilize o método de salvar um dicionário em arquivo json e a pasta já não exista.
Nela, são armazenados os arquivos json para ler e salvar na manipulação de polinômios.

## Como utilizar os métodos

* __init__: 
