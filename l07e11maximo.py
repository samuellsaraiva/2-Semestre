''' 11. Desenvolva a função maximo que recebe dois números inteiros e retorna o maior
deles. Se os números forem iguais, retorne um deles. A função main lê dois números, 
chama a função maximo passando os dois argumentos (os valores lidos) e gera 
a tela de saída com o valor retornado pela função maximo. Use variável local. ----- '''
def maximo(num1, num2):  # Definição de função
    if num2 > num1:            # Se numero2 seja maior que numero1
        maior = num2
    else:
        maior = num1
    return maior
if __name__ == '__main__':                             # Início da função main
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    vl_retorno = maximo(numero1, numero2)      # A variável maior recebe o retorno da função
    print("O maior é", vl_retorno)                     # ----- ALTERAÇÕES:
''' a. Acrescente a função le_valor, ela não recebe nada e retorna um valor lido. Leia um
valor dentro da função. Na função main, coloque comentário nos dois inputs e 
chame a função le_numero duas vezes e guarde o valor retornado nas variáveis numero1 e
 numero2. Depois chama a função maximo.
b. Troque a mensagem estática pela mensagem dinâmina dentro da função le_valor.
c. Na função principal, coloque um comentário na chamada da função maximo e 
    use uma função do Python que tem  mesma funcionalidade. 
    Use a função max que é nativa do Python.                 ----- DICAS ABAIXO:
def le_valor ():                                                                  # a.
    valor = int (input("Valor inteiro: "))
    return valor
if __name__ == '__main__':
    #numero1 = int(input("Digite o primeiro número: "))               
    #numero2 = int(input("Digite o segundo número: "))
    numero1 = le_valor ()
    numero2 = le_valor ()                                                    # a.
def le_valor (msg_dinamica):                                                                  # b.
    valor = int (input(msg_dinamica))
    return valor
    numero1 = le_valor ("Primeiro número: ")  # Na função main.
    numero2 = le_valor ("Segundo número: ")                                         # b.    
#maior = maximo(numero1, numero2)                  # c.
maior = max (numero1, numero2)                         # c.
---


d. Crie a função calculo para subtrair o maior pelo um novo numero digitado e mostre
    o resultado.                                                                    ---------- DICAS:
def calculo (numero):                                       # c.
    numero2 = int(input("digite um numero: "))
    print(numero - numero2)
calculo (maior)                                                  # c.   (na função principal)

'''
