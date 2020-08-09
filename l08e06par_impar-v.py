''' 6. Crie e carregue um vetor (array) na sua declaração com cinco valores inteiros
quaisquer. Gere a tela de saída com todos os valores armazenados no vetor, a soma
dos valores armazenados nos índices(posições) pares do vetor e a soma dos valores
armazenados nos índices(posições) ímpares do vetor. -------------   Prof. Barbosa
Saída: Soma das posições pares: 15       Soma das posições ímpares: 13                '''
vetor1 = [5, 4, 7, 9, 3]                 # Vetor com cinco valores quaisquer
tamanho = len (vetor1)                # Tamanho do vetor
soma_indice_par = 0                   # Somadores começando com 0
soma_indice_impar = 0
print ("Valores armazenados no vetor:")
print (vetor1) # print (vetor1 [ : : ] )     # Imprima cada elemento do vetor na horizontal
# Não faça assim:      soma_indice_par = vetor1 [0] + vetor1 [2] + vetor1 [4]
# Use estrutura de repetição:
for i in range(0, tamanho):                    # for i in range(tamanho):
    if i % 2 == 0:                                   # Se o índice for par?
        soma_indice_par += vetor1 [i]       # soma_indice_par = soma_indice_par + vetor1[i]
    else:
        soma_indice_impar += vetor1 [i]  # soma_indice_impar = soma_indice_impar + vetor1 [i]
print("A soma dos valores nos índices pares é:", soma_indice_par)
print("A soma dos valores nos índices ímpares é:", soma_indice_impar)
''' Alterações:
a. Mostre os valores do vetor na vertical usando o for com notação de lista.
b. Mostre os valores do vetor  na vertical usando o for com notação de vetor.
c. Refaça o programa sem usar o operador módulo ( % ). Use o for com passo 2. ---DICAS:
for valor in vetor1:                                     # a.
    print(valor)
for i in range(0, tamanho, 1):      # for i in range(tamanho):        # b.
    print(i , '  -  ', vetor1 [i])          # Imprime cada elemento do vetor na horizontal    
for i in range(0, tamanho, 2):                    # c.
    soma_indice_par += vetor1[i]         
for i in range(1, tamanho, 2):
    soma_indice_impar += vetor1 [i]    

---

'''



