''' 1. Crie a função main para lê trinta valores inteiros digitados pelo usuário e
armazene-os num vetor.
Crie a função mostra_vetor. Ela recebe o endereço do vetor, gera a tela de saída
com o conteúdo do vetor e não retorna nada. Use variável local.
- Observação: para simplificar os testes, substitua trinta por três. ------------- '''
def mostra_vetor (vet):
    print('Valores do vetor:')                # Mostra todos os valores
    print(vet)                                          # print (l_valores[ : : ])
if __name__ == '__main__':
    valores = [0] *3
    tamanho = len (valores)
    for i in range(0, tamanho):                             # Repete 3 vezes
        num = int(input("Digite um número: "))  # Recebe um número do usuário
        valores [i] = num
    mostra_vetor (valores)
''' ALTERAÇÕES:
a. Acrescente a função mostra_vetor_vertical. Ela recebe o endereço do vetor, 
    gera a tela de saída com o conteúdo do vetor na vertical e não retorna nada.
b. Na função mostra_vetor_vertical,  mostre também as respectivas posições (índices).
                                                  ----- DICAS:
def mostra_vetor_vertical (vet):         # a.
    print('Valores do vetor:')                      # Mostra todos os valores
    for i in range (0, len(vet)):
        print(vet [i])
    mostra_vetor_vertical(valores)      # a.     # No main
def mostra_vetor_vertical (vet):         # b.
    print('Posição - Valores do vetor:')          
    for i in range (0, len(vet)):
        print(i, " - ", vet [i])
    mostra_vetor_vertical(valores)      # b.     # No main
---
def mostra_vetor (vet):
    . . .
if __name__ == '__main__':
    . . .
---
Veja os vídeos abaixo:
video1 - Introdução a Listas
https://www.youtube.com/watch?v=YeaB5IgS2rY&index=25&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
video2 - Listas dentro de listas, Adicionar novos elemetos a listas(append) 
https://www.youtube.com/watch?v=zzRiX_nIIMc&index=26&list=PLfCKf0-awunOu2WyLe2pSD2fXUo795xRe
'''
