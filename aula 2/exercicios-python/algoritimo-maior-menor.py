# 4. Faça um algoritmo que receba 90000 números inteiros e verifique qual deles foi o menor e maior digitado. 
menor = None
maior = None

for i in range(90000):
    num = int(input("Insira o número: "))
    if menor is None or num < menor:
        menor = num
    if maior is None or num > maior:
        maior = num

print("Maior número:", maior)
print("Menor número:", menor)