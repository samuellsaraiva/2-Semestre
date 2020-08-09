'''       POO em Pytthon
class NomeClasse:
    def __init__ (self, p_1, p_2):                          # Método construtor
        self.nome_atributo1 = p_1
        self.nome_atributo2 = p_2
    def get_nome_atributo1 (self):           # Modelo do método get (consulta um atributo)
        return self.nome_atributo1
    def set_nome_atributo1 (self, valor): # Modelo do método set (altera valor de um atributo)
        self.nome_atributo1 = valor
    def outro_metodo (self):                      # Outros métodos da classe
        . . .
        return ...
if __name__ == '__main__':            # main <tab>
    nome_objeto1 = NomeClasse(a_1, a_2)  # Cria (instancia) o primeiro objeto da classe
    nome_objeto2 = NomeClasse(a_1, a_2)  # Cria (instancia) o segundo objeto da classe
    print ("Valor do atributo x: ", nome_objeto1.x) # nome_objeto . nome_atributo
- Com base no modelo acima, implemente estes itens:   '''
class Pessoa(object):
    def __init__(self, n, sb, id):               # Construtor
        self.nome = n                                  # Atributos
        self.sobrenome = sb
        self.idade = id
    def get_nome (self ):
        return self.nome
    def set_nome (self, n):
        self.nome = n
    def set_idade (self, id):
        self.idade = id
if __name__ == '__main__':
    pessoa1 = Pessoa("Carlos", "Pereira", 23)       # Instantiate an object of type Pessoa
    print (pessoa1)
    print(pessoa1.nome)
    pessoa2 = Pessoa("Maria", "Souza", 21)
    print(pessoa2)
    v = pessoa2.get_nome()
    print("Nome: ", v)
''' Crie a classe Pessoa 
Crie o método construtor:
    Ele recebe o self e mais três parâmetros que serão atribuídos aos atributos.
    Dentro do construtor, crie os três atributos da classe (nome, sobrenome e idade)
No método main, crie o objeto pessoa1 e passe os argumento "Carlos", "Pereira", 23
Mostre o objeto criado, o objeto pessoa1, teste (rode a classe)    # print (pessoa1)
Mostre os dados do objeto criado (os seus atriutos), teste (rode a classe)    
Dentro da classe, crie os métodos get (consultar) e set (alterar) para todos os atributos.
def get_nome_atributo1 (self):                     # Modelo do método get (consulta)
    return self.nome_atributo1
def set_nome_atributo1 (self, valor):            # Modelo do método set (altera)
    self.nome_atributo1 = valor
No main, teste os métodos gets dos atributos da classe Pessoa (consulte e mostre)
    Mostre o valor do atributo nome                   # variavel = nome_obejto.nome_metodo()
    Altere o nome do objeto pessoa1
    Mostre o valor do atributo sobrenome
    Mostre o valor do atributo idade
Use o método set para alterar o valor do atributo idade para 25, teste
Altere os atributos de modo público para modo privado. (self. __nome_atributo = p_1)
Na classe, crie o método nome_completo. Ele não recebe nada e retorna o nome completo
Dentro do programa (main) crie o objeto p2 e passe os argumento "Maria", "Souza", 21
 Mostre o valor dos atributos do objeto p2
Crie o método especial __str__
Ele não recebe nada e retorna os dados de uma pessoa (nome completo e  idade). Teste.
Crie o atributo de classe para contar a quantidade de objetos criados. Teste
class NomeClasse:
    conta = 0                                             # Atributo de classe
    def __init__ (self, p_1):                        # Método construtor
        Pessoa.conta = Pessoa.conta + 1
Na classe, crie o método compara idade.
Crie a subclasse Aluno que herda da classe Pessoa
    A classe atluno tem os atributos nome, sobrenome, idade e ra             
'''

