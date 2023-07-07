# poly_class: manipulação de polinômios

Um script em Python, com o uso das bibliotecas padrão json e pathlib, para manipulação de polinômios de qualquer grau por meio da criação da classe Polynomial. Permite avaliar o valor num ponto específico, realizar integração e derivação simbólicas, calcular a integral definida em um intervalo, obter raízes utilizando os métodos de Newton e da bisseção e ler e salvar dicionários em arquivos json para representação dos polinômios.

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

* `__init__ (self, coef_at_degree={})`: cria uma instância da classe Polynomial tomando por parâmetro coef_at_degree, dicionário cujas chaves são inteiros não negativos representando os graus e cujos valores são números (int ou float) representando os coeficientes correspondentes a esses graus. O padrão para o dicionário é um dicionário vazio, criando um polinômio nulo. Retorna None.
* `eval (self, x)`: toma por parâmetro um número (int ou float) x e avalia o polinômio nesse ponto x, retornando o valor obtido.
* `symbolic_integrate (self, constant=0)`: retorna a integral simbólica do polinômio em uma instância da classe Polynomial. O parâmetro opcional constant recebe um número (int ou float) que define o valor do coeficiente no grau 0, sendo 0 o valor padrão.
* `interval_integrate (self, interval)`: retorna o valor da integral definida no intervalo dado pelo parâmetro interval, que recebe uma tupla ou lista com dois números (int ou float) por elementos.
* `symbolic_derivative (self)`: retorna a derivada simbólica do polinômio em uma instância da classe Polynomial.
* `save_as_json (self, filename)`: salva o dicionário self.coef_at_degree correspondente ao polinômio em um arquivo json, sendo o nome dado pelo parâmetro filename e o arquivo salvo na pasta data.
* `from_json (cls, filename)`: um método de classe que cria e retorna uma instância da classe Polynomial, tomando por dicionário correspondente o lido no arquivo json, sendo seu nome dado pelo parâmetro filename e estando na pasta data.
* `newton_method (self, value, max_iterations=100, epsilon=1e-3)`: utiliza o método de Newton para obtenção de uma raiz a partir de um valor inicial dado pelo parâmetro value, um número (int ou float). Os parâmetros opcionais são: max_iterations - número que define o máximo de iterações realizado no método e cujo valor padrão é 100 - e epsilon - que define a tolerância de erro na raiz e cujo valor padrão é 1e-3. Retorna a raiz encontrada caso tenha sucesso e None caso contrário. Na possibilidade de não encontrar raiz, o método usa a função print para mostrar os parâmetros utilizados na chamada do método. Também sinaliza por print caso encontre um ponto estacionário, ou seja, um zero da derivada. O método de Newton para polinômios pode falhar por alguns motivos, como a não convergência (por um valor inicial distante de raízes ou pela formação de um loop, por exemplo), obtenção de um ponto estacionário, obtenção de uma outra raiz que não a desejada, uso do método em um polinômio sem raízes reais ou uma escolha não condizente para o número de iterações ou para o epsilon.
* `bisection_method (self, interval, iterations=100, epsilon=1e-3)`: utiliza o método da bisseção para obtenção de uma raiz a partir de um intervalo cujos valores do polinômio em seus extremos possuam sinais opostos. Recebe por parâmetros interval - intervalo definido por uma tupla ou lista com dois números (int ou float) por elementos -, iterations - número que define a quantidade de iterações realizadas e cujo valor padrão é 100 -, epsilon - número que define a tolerância de erro na obtenção da raiz. A existência de uma raiz no intervalo é garantida pelo teorema do valor intermediário. Retorna a raiz encontrada caso tenha sucesso e None caso contrário. O método pode não encontrar raiz caso o número de iterações e a tolerância escolhidos não sejam condizentes com o polinômio.

## Exemplo de uso

Exibimos um exemplo simples de uso da classe Polynomial.

```Python
from poly import Polynomial

my_poly = Polynomial({
    0: 3,
    1: -1}
    )

print(my_poly.eval(1)) # output 2
```
