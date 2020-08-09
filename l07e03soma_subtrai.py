'''    - Sintaxe do uso de função                                                  Prof. Barbosa
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

- 3. Construa o programa contendo as duas funções soma e subtrai. O programa lê
dois valores inteiros, chama a função soma passando os dois valores lidos e depois
chama a função subtrai passando os dois valores lidos. A função soma recebe dois
valores inteiros, realiza a soma deles e retorna o resultado do cálculo. A função
subtrai recebe dois valores inteiros, realiza a subtração deles e retorna o resultado
do cálculo. A função main recebe o valor retornado pelas funções soma e subtrai e
gera a tela de saída com essas informações. Use variável local.
Teste: entrada: 3 e 2. result: 5 e 1   --------------------------------------------------------- '''
def soma(a, b):                      # Definição de funções          Prof. Barbosa
    somar = a + b
    return somar
def subtrai(a, b):
    return a - b
# Início da função main.
if __name__ == '__main__':
    num1 = int(input("Digite o primeiro valor inteiro: "))                   # Recebe os valores
    num2 = int(input("Digite o segundo valor inteiro: "))
    # O retorno das funções pode substituir argumentos em outras funções
    # O próprio print() é uma função já implementada no Python que apenas utilizamos
    retorno_soma = soma (num1, num2)
    print("A soma é:", retorno_soma) # A chamada da função é usada após a criação da função
    print("A subtração é:", subtrai(num1, num2))
'''     --- ALTERAÇÕES:
a. Refaça sem usar uma variável dentro da funçao soma (somar).
b. Refaça sem usar uma variável no programa principal (retorno_soma).
c. Crie mais uma função (recebe_inteiro) para realizar o trabalho de recepção de dados
    do usuário (que é feito com int(input("..."))).
    Ela não recebe nada e retorna um valor lido.
    Chame essa função duas vezes na função principal para substituir os inputs.
d. Na função main, coloque comentário ( # ) nos dois inputs e chame a função
    recebe_inteiro duas vezes.
e. Dentro da função recebe_inteiro, troque a mensagem estática ("Digite um número inteiro")
    por uma mensagem dinâmica: "Digite o primeiro valor" ou "Digite o segundo valor"
    Altere a declaração da função recebe_inteiro. Agora ela recebe uma mensagem.
    Na função main, chame a função passando uma das mensgens acima. --- DICAS ABAIXO:
    return a + b                                                                 # a.
print("A soma é:", soma (num1, num2) )                        # b.
def recebe_inteiro ():                                                        # c.
    vl_inteiro = int(input("Digite um numero inteiro"))
    return vl_inteiro                                                           # c.
# num1 = int(input("Digite o primeiro valor inteiro: "))            # d.
# num2 = int(input("Digite o segundo valor inteiro: "))
num1 = recebe_inteiro ()
num2 = recebe_inteiro ()                                                           # d.
def recebe_inteiro (m):                                                    # e.
    vl_inteiro = int(input(m))
    return vl_inteiro                                                           
num1 = recebe_inteiro ("Digite o primeiro valor")                                           
num2 = recebe_inteiro ("Digite o segundo valor")          # e.
'''
