'''             Prof. Barbosa
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
- 4. Altere o programa anterior, agora o usuário vai escolher apenas uma operação. A
opção desejada será lida no programa que chama uma das funções(soma ou subtrai)
passando os dois valores lidos como argumen-tos.

- 5. Refaça o programa anterior, acrescente a função menu que não recebe nada e retorna
a opção digitada pelo usuário. A função main vai coordenar todo o processamento, ou
seja, a função main chama a função menu e depois chama uma das duas funções (soma 
ou subtrai).   ------------------------------------------------------------------------------------------   '''
def soma(x, y):    # Função soma. Ela recebe 2 valores e retorna a soma.
    return x + y
def subtrai(x, y):  # Função subtrai. Ela recebe 2 valores e retorna a subtração.
    calculo = x - y
    return calculo
def menu():         # Ela não recebe nada e retorna o valor digitado pelo usuário.
    opcao = int(input("Digite:\n[1] Somar\n[2] Subtrair\n"))
    return opcao
if __name__ == '__main__':
    num1 = int(input("Digite o primeiro valor: "))  # Início do programa principal.
    num2 = int(input("Digite o segundo valor: "))
    # variável retorno_oppco recebe o valor retornado pela função menu.
    retorno_opcao = menu()
     if retorno_opcao == 1:                              # para 1 chama a função soma
        print("A soma é: ", soma(num1, num2))
    elif retorno_opcao == 2:                           # para 2 chama a função subtrai
        print("A subtração é: ", subtrai(num1, num2))
    else:                                # caso seja diferente de 1 e 2, opção inválida.
        print("Opção inválida!")
'''    ALTERAÇÕES:
a. Troque as opções [1] e [2] pelos símbolos [+] e [-].  
b. Crie uma função para multiplicar e acrescente a opão multiplica no sistema.
       --- DICAS ABAIXO:             
    opcao = input("Digite:\n[+] Somar\n[-] Subtrair\n")                    # a.
if retorno_opcao == '+':   
    print("A soma é: ", soma(num1, num2))
elif retorno_opcao == '-': 
    print("A subtração é: ", subtrai(num1, num2))                            # a.
def multiplica (a , b):                                                                                # b.
    return  a * b
.  .  .
    opcao = input("Digite:\n[+] Somar\n[-] Subtrair\n[x] Multiplicar\n")
.  .  .                
elif retorno_opcao == 'x':
    print("A multiplicação é:", multiplica (num1,num2))                           # b.
'''
