'''    - 5. Refaça o programa anterior, acrescente a função menu que não recebe nada e retorna
a opção escolhida pelo usuário. O programa vai coordenar todo o processamento, ou
seja, chama a função menu e depois chama uma das duas funções (soma ou subtrai).

- 6. Use estrutura de repetição dentro da função menu para criticar a leitura da opção 
desejada. Ou seja, só sai da repetição se o usuário digitar uma das opções válidas.
Teste 1: Teste com os valores v1 = 6, v2 = 4 e 1 para somar.     Resultado: Soma: 10
Teste 2: Teste com os valores v1 = 15, v2 = 6 e 2 para subtrair. Resultado: Subtração: 9
----------------------------------------------------------------------------   Prof. Barbosa   '''
def soma(x, y):                      # Declaração das funções.
    return x + y
def subtrai(x, y):
    return x - y
def menu():
    op = input("[+] Somar\n[-] Subtrair\nDigite:")
    while (op != '+' and op != '-'):
        op = input("Digite:\n[+] Somar\n[-] Subtrair\n")
    return op                              # Fim das funções.
if __name__ == '__main__':
    retorno_opcao=menu()                                   # Início do programa principal.
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    if(retorno_opcao=='+'):
        print('Soma: ', soma(v1, v2))
    else:
        print('Sutração: ', subtrai(v1, v2))
'''ALTERAÇÕES:
a. Dentro da função menu, inclua a mensgem 'Opção inválida, tente novamente'.
b. Adicione a operação de multiplicação.
        DICAS:
def menu():                                                                 # a.
    while True:
        op = input("Digite:\n[+] Somar\n[-] Subtrair\n")
        if op == '+' or op == '-'
            break
        else
            print ('Opção inválida, tente novamente.')
    return op                                                                 # a.
def multi(x,y):                                                        # b.
	return(x*y)
--Dentro do while--
elif(op==3):
	print("Multiplicação:",multi(v1,v2))
	break                                                   # b.
-----

while True:
    op = input("Digite:\n[+] Somar\n[-] Subtrair\n")
    if op == '+' or op == '-':
        break
return op  # Fim das funções.
'''





