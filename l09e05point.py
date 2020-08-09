'''       POO em Pytthon
class NomeClasse:
    def __init__ (self):                          # Método construtor
        self.nome_atributo1
        self.nome_atributo2
    def outro_metodo (self):                # Outros métodos da classe
        return
if __name__ == '__main__':            # main <tab>
    nome_objeto1 = NomeClasse()     # Cria (instancia) um objeto da classe
    nome_objeto2 = NomeClasse()
    print ("Valor do atributo x: ", nome_objeto1.x) # nome_objeto . nome_atributo
- Com base  nos modelos acima, implemente estes itens:'''
import math
class Point:
    def __init__(self, xx=0, yy=0):  # def __init__(self, xx, yy) # Método construtor
        self.x = xx             # self.x = xx                  # Atributos
        self.y = yy              # self.y = yy
    def get_x (self):            # Modelo do método get (consulta um atributo)
        return self.x
    def set_x (self, valor):   # Modelo do método set (altera valor de um atributo)
        self.x = valor
    def distancia_origem1 (self, a, b):
        distancia = math.sqrt( (a - 0)**2 + (b - 0)**2 )    # Cálculo
        return distancia
    def distancia_origem2 (self):
        distancia = math.sqrt( (self.x - 0)**2 + (self.y - 0)**2 )    # Cálculo
        return distancia
if __name__ == '__main__':
    p1 = Point()
    print("Objeto p1 da classe Point ", p1)          #
    print("Atributo x do ponto p1= ", p1.x)          #
    print("Atributo y do ponto p1= ", p1.y)          #
    p2 = Point(2, 3)         # Instantiate an object of type Point
    print("Atributo x do ponto p2 = ", p2.x)          #
    print("Atributo y do ponto p2 = ", p2.y)          #
    print("Valor de x do p1 ", p1.get_x())  # Consulta e mostra o valor de x do ponto p
    p1.set_x(9)                         # Altera o valor de x do ponto p
    print("Valor de x do p1 ", p1.get_x())  # Consulta e mostra o valor de x do ponto p
    d1 = p2.distancia_origem1 (p2.x, p2.y)
    d2 = p2.distancia_origem2 ()
    print (d1)
    print (d2)
'''
Crie um novo projeto
Crie a classe Point.
Crie o método construtor.
O método construtor recebe o self
Dentro do construtor, crie os atributos x e y .
Dentro do contrutor, inicialize os atributos com zero.
Dentro da função main crie o objeto p (o ponto_p)
Mostre o objeto criado, o ponto p.
Rode a classe
Mostre o valor do atributo x
Mostre o valor do atributo y
Dentro da função main crie o segundo objeto da classe Ponto, objeto  m (o ponto_m)
Altere o valor do atributo x para 9 do primeiro objeto (objeto p)
Teste o item anterior
Rode a classe
Dentro da função main crie o objeto q passando o valor do atributo x
Mostre os atributos do ponto q
Altere o construtor para ele receber o valor do atributo x e do atributo y
Atualize as atribuições dentro do método construtor
Dentro da classe, crie os métodos get (consultar) e set (alterar) para os atributos x e y.
def get_nome_atributo (self):           # Modelo do método get (consulta um atributo)
    return self.nome_atributo
def set_nome_atributo (self, valor): # Modelo do método set (altera valor de um atributo)
    self.nome_atributo = valor
No main, teste os métodos gets e sets dos dois atributos da classe Point
Na classe, crie o método distância do ponto para origem (0, 0) do plano cartesiano.
distancia = raiz_quadrada ( ( x1-x2)2 + (y1-y1)2 )
Teste1: x = 2 e y = 3       distancia = 3.60
Teste1: x = 3 e y = 5       distancia = 5.83
'''

