''' 10. Precisamos realizar uma pesquisa para encontrar o maior valor armazenado
num vetor de trinta posições. Carregue o vetor com números reais quaisquer de 
uma das maneiras possíveis. Gere a tela de saída com o conteúdo do vetor (todos 
os valores armazenados no vetor) e o maior valor encontrado. 
Não use as funções sort e max do Python. Resolva usando lógica. -Prof. Barbosa '''
import random
vetor = [0] *10                                  # Cria o vetor com 10 valores (zeros) pra facilitar
tamanho = len(vetor)
for i in range(0, tamanho):                  # Preenche o vetor com valores aleatórios
    sorteio = random.uniform(0, 100)    # Gera números reais.
    vetor [i] = sorteio
print ("Posição - 2 casas decimais - Várias casas decimais:") # Cabeçalho.
for i in range(0, tamanho):                  # Mostra o vetor preenchido         print (vetor)
    print ("%d   -   %.2f   -   %f " %(i, vetor [i], vetor [i]))
maior = vetor[0]                   # Assume que o maior elemento do vetor é o primeiro
for i in range(0, tamanho):    # Percorre a vetor
    if vetor[i] > maior:           # Se o valor no vetor for maior do que o maior
        maior = vetor[i]           # Atualiza o maior valor
print("O maior é ", maior)  # No final, mostra o maior valor.        # ALTERAÇÕES:
''' a. Acrescente o menor valor.                                                        
b. Acrescente também a soma e a média dos valores armazenados.----- DICAS:   
maior = vetor[0]  # O maior elemento do vetor é o primeiro              # a.
menor = vetor[0]  # O menor elemento do vetor é o primeiro 
for i in range(0, tamanho):  # Percorre a vetor
    if vetor[i] > maior:  # Se o valor lido atualmente for maior do que o maior já registrado
        maior = vetor[i]  # O novo maior valor passa a ser ele
    if vetor[i] < menor:  # Se o valor lido atualmente for menor do que o menor já registrado
        menor = vetor[i]  # O novo menor valor passa a ser ele
for i in range(0, tamanho):  # Percorre a vetor                               # b.
    soma += vetor [i]
    if vetor[i] > maior:  # Se o valor lido atualmente for maior do que o maior já registrado
        maior = vetor[i]  # O novo maior valor passa a ser ele
media = soma / tamanho
print (soma)
print (media)


'''
