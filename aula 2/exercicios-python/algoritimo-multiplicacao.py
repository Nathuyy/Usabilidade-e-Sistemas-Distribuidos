# 1. Faça um algoritmo que calcule a multiplicação entre dois números sem utilizar o sinal de multiplicação ( * ) ou função. Utilize estrutura de repetição e soma.

def multiplicar(multiplicando, multiplicador):
    resultado = 0
    contador = 0

    while contador < multiplicador:
        resultado += multiplicando
        contador += 1

    return resultado


print("Multiplicacao:", multiplicar(4, 5))