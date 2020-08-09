'''     Prof. Barbosa
- Sintaxe do uso de função
def nome_funcao (par1, par2, ... , parn):    # par (parâmetro) - o que a função recebe
    script                                                          # indentação obrigatória. 
    .  .  .
    return val1, val2, ... , valn
def --> declara que estamos construindo uma funçao
nome_funcao --> nome da função definido pelo desenvolvedor
 script --> código da função
return --> indica o fim da função e o que estará sendo retornado
val1, val2, ... , valn --> Valores retornados
- Chamada da função:
nome_funcao (arg1, arg2, ... , argn)            # arg (argumento) - o que envio para a função
- Exemplo:
print() é uma função, ou seja, a ideia de criar uma função é a sua reutilização 
em vários momentos do programa

- 1. Crie a função para somar dois valores inteiros. Ela recebe dois valores e retorna
o resultado do cálculo. A função main lê os valores, chama a função soma passando os
valores lidos e depois mostra o valor retornado pela função soma, ou seja, o
resultado obtido. Use variável local.
- Teste: Entrada: 3 e 2. resultado: 5
'''
# Define a função soma, que recebe os parâmetros a e b
# A definição da função não é executada. Ela só será executada quando for
# chamada (na linha retorno = somae  (valor1, valor2) )
def soma(a, b):                                              # Prof. Barbosa
    valor = a + b                              # valor recebe a soma dos parâmetros recebidos
    return valor                                   # retorna o valor calculado
# Fim da funçao soma.
if __name__ == '__main__':             # main <tab>
    valor1 = int (input  ('Primeiro valor: ') )
    valor2 = int (input  ('Segundo valor: ') )
    vl_retorno = soma (valor1, valor2) # A chamada da função é realizada após a criação da função.
    print("A soma é: ", vl_retorno)
'''     ALTERAÇÕES:
a. Substitua os dois valores inteiros digitados pelo usuário e passados para função por
estes dois valores reais (2.1, 3.3).
b. Refaça a função soma sem utilizar a variável dentro da função soma.
c. Refaça o print sem utilizar a variável vl_retorno                       DICAS ABAIXO:
retorno = soma (2.1, 3.3)                              # a.
def soma(a, b):                                             # b.
    return a + b                                              # b.
print ("A soma é:", soma(valor1, valor2))   # c.
'''
