''' 13. Projete a função potencia que recebe dois valores inteiros, a base e o expoente,
e retorna o valor da potência correspondente. A função main lê o valor da a base e 
do expoente, chama a função potencia passando os dois argumentos (os valores lidos) 
e mostra o valor retornado pela função potencia. Considere que a base pode ser um 
valor inteiro positivo, nulo ou negativo e o expoente, um inteiro positivo ou nulo. 
Não use o ** e nem a função pow da linguagem. E use variável local. 
Teste 1: base = 2, expoente = 3               potência = 8
Teste 2: base = 2, expoente = 4               potência = 16
Teste 3: base = 3, expoente = 2               potência =  9            -------   Prof. Barbosa   '''
def potencia(x,  y):
    valor_potencia = 1
    for i in range (1, y+1):
        valor_potencia *= x
    return valor_potencia;                                   # Retorna o resultado
if __name__ == '__main__':
    v1 = int (input ("Valor 1: "))
    v2 = int (input ("Valor 2: "))
    r = potencia(v1,v2)
    print("Potência:" , r)                            # ALTERAÇÕES:
''' a. Na função principal, coloque um comentário na chamada da função potencia e 
    use uma função do Python que tem  mesma funcionalidade. 
    Use a função pow ou operador **  que é nativa do Python.        ----- DICAS ABAIXO:
-----
def potencia(x,  y):

    #      Desenvolva o código da função.

    return valor_potencia;                                   # Retorna o resultado
if __name__ == '__main__':
    v1 = int (input ("Valor 1: "))
    v2 = int (input ("Valor 2: "))
    r = potencia(v1, v2)
    print("Potência:" , r)
-----
    v1 = potencia (2,4)
    print("Potência" , v1)
    v2 = potencia (3,2)
    print("Potência" , v2)
-----
 import math 
 math.pow(2,3) 

'''











