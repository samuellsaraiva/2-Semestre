''' 10. No exercício anterior, crie mais uma função com o objetivo de lê um valor real.
Ela não recebe parâmetro e retorna um float. A função le_numero deve ser chamada
duas vezes pela função main.
Comente os dois inputs da função main e chame a função le_numero duas vezes.
if __name__ == '__main__': 
    #numero1 = float(input("Digite um número: "))        # Recebe os números
    #numero2 = float(input("Digite um número: "))                 -------------------   '''
def le_numero():                  # A função não recebe nada e retorna um valor
    valor = input("Digite uma valor: ")
    valor = float(valor)
    return valor
if __name__ == '__main__':
    #numero1 = float(input("Digite o primeiro valor: "))
    #numero2 = float(input("Digite o segundo valor: "))
    numero1 = le_numero();
    numero2 = le_numero();
    vl_retorno = comparaValores(numero1, numero2)     # Recebe a resposta da função
    #  . . .                            Igual ao programa anterior.
''' ALTERAÇÕES:
a. Troque a mensagem estática por uma mensagem dinâmica dentro da função le_numero.
        DICAS:
def le_numero(mensagem):                                                             # a.
    valor = input(mensagem)     # valor = float(input(mensagem))
    valor = float(valor)
    return valor
if __name__ == '__main__':
    #numero1 = float(input("Digite o primeiro valor: "))        
    #numero2 = float(input("Digite o segundo valor: "))
    numero1 = le_numero("Digite o primeiro valor: ");
    numero2 = le_numero("Digite o segundo valor: ");
    vl_retorno = comparaValores(numero1, numero2)     
    #  . . .                            Igual ao programa anterior.                   # a.






b - Obtenha o mesmo resultado com apenas 1 linha de código dentro da função
DICAS:
def leNumero():
    return float(input("Digite uma valor: "))

'''



