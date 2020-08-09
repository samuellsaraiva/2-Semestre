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
- 3. Construa o programa contendo as funções soma e subtrai. O programa lê
dois valores inteiros, chama a função soma passando os dois valores lidos e depois
chama a função subtrai passando os dois valores lidos. A função soma recebe dois
valores inteiros, realiza a soma deles e retorna o resultado do cálculo. A função
subtrai recebe dois valores inteiros, realiza a subtração deles e retorna o resultado
do cálculo. O programa recebe o valor retornado pelas funções soma e subtrai e
gera a tela de saída com essas informações. Use variável local.

- 4. Altere o programa anterior, agora o usuário vai escolher apenas uma operação.
A opção desejada será lida no programa que chama uma das funções(soma ou subtrai)
passando os dois valores lidos como argumentos.
Teste 1: valores v1 = 13, v2 = 14 e opcao = 1.   Resultado: Soma: 27 
Teste 2: valores v1 = 13, v2 = 14 e opcao = 2.   Resultado: Subtração: -1   
Teste 3: valores v1 = 13, v2 = 14 e opcao = 3.   Resultado: Opção inválida   ------------- '''
def soma(x, y):                     # Função soma. Ela recebe 2 valores e retorna a soma.
    return x + y
def subtrai(x, y):                   # Função subtrai. Ela recebe 2 valores e retorna a subtração.
    calculo = x - y
    return calculo
if __name__ == '__main__':                                        # main <tab>
    v1 = int(input("Digite o primeiro valor: "))            # Início da função main.
    v2 = int(input("Digite o segundo valor: "))
    opcao = int(input("Digite:\n[1] Somar\n[2] Subtrair\n"))
    if(opcao==1):      # Se o usuário digitou 1, chama a função soma, senão, a função subtrai
        print('Soma: ', soma(v1, v2))
    else:
        print('Subtração: ', subtrai(v1, v2))
'''    ALTERAÇÕES:
a. Mostre também uma mensagem de opção inválida.
b. Use a função 'soma' para somar 4 valores e mostre o resultado. 
    Não mexa (altere) na função soma.                                        ---- DICAS ABAIXO:    
elif (opcao == 2):                                              # a.
    print('Subtração: ', subtrai(v1, v2))
else:
    print ('Opção inválida')                                # a.
print (soma(v1, v2) + soma(v3, v4))                       # b.    Solução 1
print (soma ( soma(v1, v2), soma(v3, v4) ) )          # b.    Solução 2
---

def subtrai (x, y):                                             # c.
    . . .
    print ('Subtração: ', subtrai (y=2, x=5) )                Solução 1
    print ('Subtração: ', subtrai (y=v1, x=v2) )   # c.    Solução 2

'''


