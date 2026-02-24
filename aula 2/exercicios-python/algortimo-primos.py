# 6. Faça um algoritmo que receba somente números inteiros, positivos e maiores que zero. O algoritmo deve verificar se o número informado é primo ou não.

def verificaSeEhPrimo(numero):
    if numero == 1:
        print("nao é primo")

    for i in range(2, numero):
        if numero % i == 0:
            print("não é primo")
            return
    print("é primo")


def verificaNumeroValido(numero):
    if numero > 0:
        return True
    else:
        return False

numero = int(input("Insira um número: "))

if(verificaNumeroValido(numero)):
    verificaSeEhPrimo(numero)