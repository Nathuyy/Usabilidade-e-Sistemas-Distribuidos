def eh_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    return True


total_numero = int(input("Insira uma quantidade de números: "))

numeros = []

for i in range(total_numero):
    numero = int(input("\nInsira o número: "))
    numeros.append(numero)

primos = []
primos_maior_1000 = 0

for numero in numeros:
    if eh_primo(numero):
        primos.append(numero)
        
        if numero > 1000:
            primos_maior_1000 += 1


if len(primos) > 0:
    maior = max(primos)
    menor = min(primos)
    media = sum(primos) / len(primos)
    
    print("\nQuantidade de primos maiores que 1000:", primos_maior_1000)
    print("Maior primo:", maior)
    print("Menor primo:", menor)
    print("Média dos primos:", media)
else:
    print("\nNenhum número primo foi digitado.")