''' 9. Projete a função compara_valores que recebe dois números reais e retorna um valor
inteiro. Ela retorna o valor zero, se os números recebidos forem iguais; retorna o
valor +1, se o primeiro número recebido for maior que o segundo e retorna o valor
-1, se o primeiro número recebido for menor. A função main lê os dois números reais,
chama a função comparaValores passando os dois números lidos e com o valor retornado
pela função compara_valores mostra uma destas mensagens “Os valores são iguais.”,
“O primeiro valor é maior.” ou “O segundo valor é maior.”. Use variável local.   
Teste 1: Entrada: valor1 = 5, valor2 = 4          Saída: O primeiro valaor é o maior
Teste 2: Entrada: valor1 = 4, valor2 = 5          Saída: O segundo valaor é o maior
Teste 3: Entrada: valor1 = 4, valor2 = 4          Saída: Os valores são iguais.   ---------------   '''
def comparaValores(numero1, numero2):
    if numero1 > numero2:
        resposta = 1
    elif numero1 == numero2:
        resposta =0
    else:
        resposta = -1
    return resposta
if __name__ == '__main__':
    numero1 = float(input("Digite um número: "))        # Recebe os números
    numero2 = float(input("Digite um número: "))
    vl_retorno = comparaValores(numero1, numero2)     # Recebe a resposta da função
    print(vl_retorno)                                                       # Mostra o resultado
'''     ALTERAÇÕES:
a. Na função main, mostre uma das três mensagens indicadas no enunciado.
b. O retorno de funções pode ser utilizado diretamente no argumento de outras
funções, desde que o tipo seja mantido. Refaça toda a função main (com exceção da
definição da função comparaValores) em uma única linha utilizando essa propriedade.
    --- DICAS ABAIXO:
if vl_retorno == 1:                                            # a.
    print ("O primeiro valor é o maior');
elif vl_retorno == 0:
    print ("Os valores são iguais")
else
    print ("O segundo valor é o maior');           # a.
Ou seja, refaça a função main sem usar as variáveis vl_retorno, numero1 e numero2.  # b.
print(comparaValores(float(input("Digite um número: ")),float(input("Digite um número: "))))

---
def comparaValores(numero1, numero2):
    if numero1 > numero2:
        return 1
    elif numero1 == numero2:
        return 0
    else:
        return -1

'''
