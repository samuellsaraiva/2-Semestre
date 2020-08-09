''' 7. Desenvolva a função positivo_nulo_negativo que recebe um número qualquer real
e retorna um valor inteiro. Ela retorna o valor +1, se o número recebido for positivo;
ela retorna o valor zero, se o número recebido for nulo e ela retorna o valor -1,
se o número recebido for negativo. A função main lê o número, chama a função
positivo_nulo_negativo passando o valor lido (argumento) e com o valor retornado pela
função, mostre uma mensagem apropriada. Use variável local.
Teste 1: Entrada  7               Saída  1
Teste 2: Entrada -7               Saída -1   -------------------------------------   Prof. Barbosa   '''
def positivo_nulo_negativo(numero):   # Definição da função.
    if numero < 0:
        ret = -1
    elif numero == 0:
        ret = 0
    else:
        ret = 1
    return ret
if __name__ == '__main__':              # Início da função main.
    valor = float(input("Digite um número: "))
    resposta = positivo_nulo_negativo(valor)       # recebe a resposta da função
    print("Resposta:", resposta)
'''    Alterações:
a. Refaça o exercício sem usar a variável resposta, na função main.
b. Refaça o exercício sem usar a variável valor, na função main.
c. Acrescente a função positivo_nulo_negativo_2 que recebe um número e não retornar 
nada. Ela mostra uma das mensagens: "Número positivo", "Número negativo" ou 
"Número nulo".                                              ----- DICAS ABAIXO:

#resposta = positivoNuloNegativo(valor)                   # a.
#print("Resposta:", resposta)
print("Resposta:", positivoNuloNegativo(valor))
#valor = float(input("Digite um número: "))              # b.
#resposta = positivoNuloNegativo(valor)
#print("Resposta:", resposta)
#print("Resposta:", positivoNuloNegativo(valor))
print("Resposta:", positivoNuloNegativo(float(input("Digite um número: "))))
def positivo_nulo_negattivo (number):              # c.
    if number < 0:  
        print("Numero negativo")
    elif number == 0:
        print("Numero nulo")
    else:
        print("Numero positivo")                     
valor = float(input("Digite um número: "))                  # Função main
positivo_nulo_negativo(valor)                           # c.
'''
