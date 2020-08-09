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
-------------------------------------------------------------------------------------------------------
- Com base no modelo acima, implemente estes itens:
- Crie a classe ContaCorrente, com estes atributos: titular, numero, saldo
- Crie o construtor da classe
- No main, crie o primeiro objeto da classe (a primeira conta corrente) com estes dados:
 'João', '123-4', 1000.00  
- No main, consulte os dados do objeto criado. Ex.: nome_objeto.nome_metodo()
- Altere o número da conta corrente para 923-4. Ex.: nome_objeto.nome_metodo(valor)
- Verifique se a alteração anterior foi bem-sucedida.
- Transforme os atributos em atributos privados. self.__titular = tit
- Crie os métodos get_numero e set_numero.
- Crie o método deposito, ele recebe um valor e acrescenta ao saldo.
- No main, realize um deposito. Verifique se o deposito foi bem-sucedido.
- Crie o método retirada, ele recebe um valor e subtrai do saldo.
- No main, realize uma retirada. Verifique se a retirada foi bem-sucedido.
- Verifique se o correntista pode realizar o saque.
- Crie a conta2 (o segundo objeto) com os valores digitados pelo usuário. 
- Transferência entre duas contas'''
class ContaCorrente(object):
     def __init__(self, tit = "", num = "", saldo=0.0):      # Construtor
        self.titular = tit                         # Atributos
        self.numero = num
        self.saldo = saldo
     def get_titular(self):                      # Métodos
        return self.titular
     def set_titular (self, v):
        self.titular = v
     def get_numero(self):
        return self.numero
     def set_numero (self, v):
        self.numero = v
     def get_saldo(self):
        return self.saldo
     def deposito(self, valor):
        self.saldo += valor
     def retirada(self, valor):
        self.saldo = self.saldo - valor
if __name__ == '__main__':
    conta1 = ContaCorrente('João', '123-4', 1000.00) # Cria o objeto conta1.
    print ("Titular:", conta1.titular)             # Com atributo global
    print ("Titular:", conta1.get_titular())    # Com atributo privado
    print("Titular:", conta1.deposito(120.00))  # Com atributo privado













