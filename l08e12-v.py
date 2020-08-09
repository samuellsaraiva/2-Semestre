''' 12. Desejamos realizar a pesquisa sequencial em um vetor de trinta elementos.
Carregue o vetor de uma das maneiras possíveis. O programa lê o valor 
a ser pesquisado e mostra a mensagem “O valor foi encontrado" ou mostra
a mensagem “O valor não foi encontrado.”.        -----------           Prof. Barbosa   '''
import random
dados = [0] *10
tamanho = len(dados)
for i in range(0, tamanho):                  # Preenche o vetor com valores aleatórios
    sorteio = random.randint(0, 5)    # Gera números inteiros.
    dados [i] = sorteio
#recebe o número e grava na variável valor
valor = int (input("Digite o número a ser pesquisado: "))
b = False
for l in dados:
    if (l == valor):
        print("Encontrou")
        b = True
        break
if b == False:
    print ("Não encontrou")
'''ALTERAÇÕES:
a. Para testar o programa, mostre todos os elementos do vetor antes de receber
 o número do usuário. Teste digitando um valor que está no vetor e também 
 com um valor que não existe.
Teste1: Se o elemento estiver no vetor. 
            Resultado esperado: O valor foi encontrado.
Teste2: Se o elemento não estiver no vetor. 
            Resultado esperado: O valor não foi encontrado.
b. Melhore o programa, se o valor estivere no vetor, mostre a mensagem e a
    posição onde o valor está armazenado .            
'''
'''RESOLUÇÕES:
a.
#Antes de receber o número do usuário
	print(dados)
b. 
'''
