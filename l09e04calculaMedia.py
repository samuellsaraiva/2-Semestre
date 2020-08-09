''' 4. Crie a função calcula_media. Ela recebe o endereço do vetor, calcula
a média dos valores do vetor e retorna o valor da média.
Crie a função main para lê trinta valores inteiros digitados pelo usuário e
armazene-os num vetor. Chame a função calcula_media e mostre o valor
retornado pela função.
- Observação: para simplificar os testes, substitua trinta por três.   ---------- '''
def calcula_media (vetor):
    soma = ct = 0  # valor da soma inicialmente zero
    for i in range(0, 2 + 1):     # for i in range(0, 3):               # Repete 3 vezes
        soma = soma + vetor[i]  # soma += vetor[i]
        ct += 1
    media = soma / ct
    return media
if __name__ == '__main__':
    notas = [0 ] * 3
    tamanho = len (notas)
    for i in range(0, tamanho):
        valor = int(input("Digite a nota do aluno: "))  # recebe a nota
        notas[i] = valor
    media = calcula_media (notas)
    print("A média é:", media)        # mostra a média
''' ----- Alterações:
a. Acrescente a função mostra_vetor. Ela recebe o endereço do vetor, gera a 
tela de saída com o conteúdo do vetor e não retorna nada. Use variável local.
b. Acrescente a função carrega_vetor. Ela não recebe nada,  recebe os valores 
    do usuário e retorna o enderço do vetor.       
    ----- DICAS:
def mostra_vetor (vet):                               # a.
    print('Valores do vetor:')                
    print(vet)                                          
mostra_vetor(notas)                                    # a.    
def carrega_vetor ():                                   # b.
    valores = [0] *3
    for i in range(0, 2+1):                                    #for i in range(0, 3):  # Repete 3 vezes
        num = int(input("Digite um número: "))  
        valores [i] = num
    return valores
    v = carrega_vetor()                                  # b.    # No main
---
        #notas.append(valor)  # adiciona à lista
'''
