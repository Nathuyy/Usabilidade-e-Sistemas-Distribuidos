"""
5.Escreva um algoritmo que leia um número n (número de termos de uma progressão aritmética), a1 ( o primeiro termo da progressão)
e r (a razão da progressão) e escreva os n termos dessa progressão, bem como a soma dos elementos.
"""

numeroN = int(input("Insira o número n: "))
a1 = int(input("Insira o número a1: "))
r = int(input("Insira o número da razão (r): "))

def calcularSomaElementos(numeroN, a1, r):
    an = calcularAn(numeroN, a1, r)
    return ((a1 + an) * numeroN ) / 2

def calcularAn(numeroN, a1, r):
    return a1 + (numeroN - 1) * r

def listarNtermos(numeroN, a1, r):
    for i in range(numeroN):
        termo = a1 + i * r
        print(termo)


print("\nTermos da PA:")
listarNtermos(numeroN, a1, r)

soma = calcularSomaElementos(numeroN, a1, r)
print("\nSoma dos elementos:", soma)