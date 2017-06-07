"""
    Numero Primos: Numeros primos são numeros que tem apenas 2
    divisores o 1 e ele mesmo.
    Exemplo numero: 2 pode se dividir por 1 e por ele mesmo
"""

def isprimo(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c = c + 1
    if c == 2:
        return True
    else:
        return False
numero = int(input("Digite um Numero para verificar se é primo: "))
a = isprimo(numero)
if a:
    print("O Numero é primo")
else:
    print("O Numero não é primo")


        
