''' 6. Crie e carregue um vetor (array) na sua declaração com cinco valores inteiros
quaisquer. Gere a tela de saída com todos os valores armazenados no vetor, a soma
dos valores armazenados nos índices(posições) pares do vetor e a soma dos valores
armazenados nos índices(posições) ímpares do vetor.   -------------   Prof. Barbosa

7. Refaça o exercício anterior, carregue o vetor com valores sorteados pelo
compilador entre 0 e 9.
- Sintaxe para sortear números:
import random
...
vl_sorteado = random.randint (vl_inicial, vl_final)
Descrição: Sorteia um número inteiro no intervalo fechado de vl_inicial a vl_final.
Lembre-se que o número sorteado deve ser armazenado na memória numa variável.   '''
import random
vetor = [0] * 5                                 # Carrega o vetor com cinco zeros
tamanho = len(vetor)
for i in range(0, tamanho):
    vl_sorteado = random.randint(0, 9)
    vetor [i] = vl_sorteado
print (vetor) # print (vetor[ : : ] )        # Imprima cada elemento do vetor na horizontal
soma_indice_par = 0                         # Somadores começando com em 0
soma_indice_impar = 0
for i in range(0, tamanho, 1):
    if i % 2 == 0:                                 # Se o índice for par?
        soma_indice_par += vetor [i]      # soma_indice_par = soma_indice_par + lista [i]
    else:
        soma_indice_impar += vetor [i]  # soma_indice_impar = soma_indice_impar + lista [i]
print("A soma dos valores nos índices pares é:", soma_indice_par)
print("A soma dos valores nos índices ímpares é:", soma_indice_impar)
'''     ALTERAÇÕES:                        # Prova P1, turma A: 19/08
a. Mostre os valores do vetor na vertical usando o for com notação de lista.
b. Mostre os valores do vetor  na vertical usando o for com notação de vetor.
c. Refaça o programa sem usar o operador módulo ( % ). Use o for com passo 2.
d. Altere o valor dos números sorteados de 10 a 15.
e. Altere o valor dos números sorteados de -2 a +2.                     ----- DICAS:
for valor in vetor:                                          # a.      Notação de lista.
    print(valor)
for indice in range (0, tamanho, 1):               # b.      Notação de vetor.
    print ( vetor [indice] )
for i in range(0, tamanho, 2):                         # c.
    soma_indice_par += vetor [i]       # soma_indice_par = soma_indice_par + vetor [i]
for i in range(1, tamanho, 2):
    soma_indice_impar += vetor[i]     # soma_indice_impar = soma_indice_impar + vetor[i]
    vl_sorteado = random.randint(10, 15)       # d.
    vl_sorteado = random.randint(-2, 2)          # e.
'''
