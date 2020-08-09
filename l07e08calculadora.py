''' 8. Simule uma calculadora com as quatro operações aritméticas. Implemente uma
função para cada operação aritmética. Ela recebe dois valores e não retorna nada.
O usuário fornecerá a operação desejada(operador: +, -, x, / )
e os dois valores dentro do programa que chamará uma das quatro funções.
O resultado do cálculo será mostrado dentro de cada função. Use variável local.
Teste 1. Teste com os valores a = 45 , b = 89 e op = +. Resultado Esperado:134
Teste 2. Teste com os valores a = 67, b = 45 e op = -.   Resultado Esperado:22
Teste 3. Teste com os valores a = 23, b = 8 e op = *.     Resultado Esperado:184
Teste 4. Teste com os valores a = 230, b = 4 e op = /.   Resultado Esperado:57.5  ---- '''
def soma(x, y):               # Definição das funções.
    print('Soma: ', x+y)
    return
def subtracao(x, y):
    print('Subtração: ', x-y)
def multiplicacao(x, y):
    print('Multiplicação:', x*y)
    return
def divisao(x, y):
    print('Divisão: ', x/y)
if __name__ == '__main__':                         # Início da função main.
    valor1 = float(input("Digite primeiro valor: "))
    valor2 = float(input("Digite segundo valor: "))
    op = input("Digite o operador [+] [-] [x] [/]: ")
    if(op=="+"):
        soma(valor1, valor2)
    elif(op=="-"):
        subtracao(valor1, valor2)
    elif(op=="x"):
        multiplicacao(valor1, valor2)
    else:
        divisao(valor1, valor2)                                 #   ----- ALTERAÇÕES:
''' a. Inclua a mensagem de  opção inválida.
b. Acrescente a função soma_2, ela recebe dois valores, faz o cálculo e retorna o 
    resultado do cálculo. Ela não imprime nada. 
c. Chame a função soma e soma_2, quando o usuário escolher a opção somar.
     --- DICAS ABAIXO:
. . .                                        # a.
elif (op=="x"):
    multiplicacao(a, b)
elif (op=="/"):
    divisao(a, b)
else
    print ('Opção inválida')
def soma_2 (x, y):                 # b.
    return x+y
if (op=="+"):                            # c.           Na função main
    soma(a, b)
    print (soma_2 (a, b))            # c.

'''


