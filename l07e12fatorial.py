''' 12. Elabore a função fatorial que recebe o valor inteiro e retorna seu fatorial. O valor
será lido no programa que chama a função fatorial passando o valor lido. o programa
recebe o valor retornado pela função fatorial e gera a tela de saída. Use variável local.
Lembre-se que fatorial de n ( n!) é a multiplicação dos números naturais de 1 até n.
0! = 1,            1! = 1,                n! = 1 x 2 x 3 x . . . x (n - 1) x n.
Teste 1: Entrada v = 3. Resultado: Fatorial de 3 = 6
Teste 2: Entrada v = 4. Resultado: Fatorial de 4 = 24
Teste 3: Entrada v = 5. Resultado: Fatorial de 5 = 120
Teste 4: Entrada v = 8. Resultado: Fatorial de 8 = 40320   --------------   Prof. Barbosa   '''
def fatorial (n):                       # A função que recebe um valor e retorna o fatorial.
    resultado =1
    for x in range (1, n+1, 1):
        resultado = resultado * x
    return resultado
if __name__ == '__main__':                                # Início da função main
    v = int(input("Digite um valor: "))
    retorno = fatorial (v)
    print("Fatorial de", v , "=", retorno)                # ----- ALTERAÇÕES:
''' a. Refaça sem usar a variável retorno.
b. Se o valor digitado for negativo, mostre uma mensagem apropriada.
c. Adicione o valor 3 como default para o parâmentro n da função fatorial, 
   ou seja, o n será 3 se nenhum valor for passado na chamada da função.
d. Usando a função fatorial, calcule e mostre o fatorial do fatorial de 3.   ----- DICAS:
#retorno = fatorial (v)                                                # a.
print("Fatorial de", v , "=", fatorial (v) )                   # a.
if v >= 0:                                                                 # b.
    print("Fatorial de", v , "=", fatorial (v) )
else:
    print ("Digite um valor maior ou igual a zero")  # b.
def fatorial (n=3):                                                              # c.
    . . .
retorno = fatorial ( ) # Na função main.                             # c.
print (fatorial (fatorial(3) ) )                                        # d.
---
def fatorial(n):                       # A função que recebe um valor e retorna o fatorial.

    #      Desenvolva o código da função.
'''
