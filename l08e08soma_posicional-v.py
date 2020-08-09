''' 8. Elabore o programa que faça a soma posicional entre dois vetores de valores
inteiros de cinquenta posições e armazene o resultado do cálculo num terceiro vetor.
Carregue(armazene) os valores nos dois vetores de uma das maneiras possíveis e
mostre na tela de saída o conteúdo das três listas. Lembrando que a soma posicional
vai somar o conteúdo da posição 0 do primeiro vetor com o conteúdo da posição 0 do
segundo vetor e o resultado é armazenado na posição 0 do terceiro vetor. E assim
sucessivamente.
Obs. resolva primeiro com cinco valores para facilitar os testes de desenvolvimento. '''
import random
tamanho = 5
vetor_a = [0] * tamanho                         # Inicialização dos vetores
vetor_b = [0] * tamanho
vetor_soma = [0] * tamanho
for i in range(0, tamanho):               # Preenche a vetor_a com valores aleatórios
    vl_aleatorio = random.randint(0, 9)
    vetor_a [i] = vl_aleatorio
for i in range(0, tamanho):               # preenche a vetor_b com valores aleatórios
    vl_aleatorio = random.randint(0, 9)
    vetor_b [i] = vl_aleatorio
for i in range(0, tamanho):        # preenche a vetor_soma com as somas correspondentes
    soma = vetor_a[i] + vetor_b[i]
    vetor_soma [i] = soma
print (vetor_a )               # print (vetor_a [ : : ] )
print (vetor_b )               # print (vetor_b [ : : ] )
print (vetor_soma)          # print (vetor_soma [ : : ] )
''''     Alterações:
a. Essa solução utiliza três loops (fors) para cumprir todas as tarefas.
    Refaça-a utilizando apenas um for.
b. Use notação de lista e mostre os valores do vetor soma na vertical.
c. Use notação de vetor e mostre os valores do vetor soma na vertical.
d. Mostre a soma dos valores armazenados no vetor soma.     ----- DICAS:     
for i in range(0, tamanho):                                                     # a.
    vl_aleatorio = random.randint(0, 9)
    vetor_a [i] = vl_aleatorio
    vl_aleatorio = random.randint(0, 9)
    vetor_b [i] = vl_aleatorio
    soma = vetor_a[i] + vetor_b[i]
    vetor_soma [i] = soma
for valor in vetor_soma:         # mostra a vetor_soma na vertical            # b.
    print (valor)
for i in range(0, tamanho):     # mostra a vetor_soma na vertical            # c.
    print (vetor_soma [i] )   
for vl_elemento in vetor_soma:           # Usando notação de lista.
    print(vl_elemento)

---

#tamanho = len(vetor_a)                                   # O tamanho dos vetores
'''
