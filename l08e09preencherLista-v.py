''' 9. Construa o programa que preencha um vetor de dez elementos inteiros,
coloque "1" nas posições pares (índices pares) e "0" nas posições ímpares
(índices ímpares). Mostre o vetor gerado. -------------------   Prof. Barbosa   '''
v_inteiros = [0] * 10                         # Cria o vetor v_inteiros e carrega com 10 zeros
tamanho = len(v_inteiros)
for indice in range(0, tamanho):    # para indice de 0 a 9
    if indice % 2 == 0:            # Se índice for par, acrescenta o valor 1
        v_inteiros [indice] = 1
    else:                                  # Se índice for ímpar, acrescenta o valor 0
        v_inteiros [indice] = 0
print (v_inteiros)                     #print (v_inteiros [ : : ])
''' ALTERAÇÕES:
a. Mostre a lista gerada na vertical usando notação de lista. 
b. Mostre a lista gerada na vertical usando notação de vetor. Use in range 
c. Mostre também o índice de cada elemento.             ----- DICAS:
for elemento in l_inteiros:                     # a.
    print(elemento)
for i in range (0, tamanho, 1):                     # b.
    print(v_inteiros [i])
for i in range (0, tamanho, 1):                     # c.
    print(i, "  -  ', v_inteiros [i])

# Outra solução, usando notação de lista:
indice = 0                                               # c
for elemento in l_inteiros:                    
    print(indice, ' - ', elemento)
    indice = indice + 1
'''
