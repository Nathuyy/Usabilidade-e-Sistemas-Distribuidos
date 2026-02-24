"""
2. Faça um algoritmo com as funções de um caixa eletrônico. Utilize estrutura de repetição. 
- Deve apresentar um menu:
1 - Saldo
2 - Saque
3 - Depósito
4 - Sair
- O algoritmo deve executar as operações de um cliente até que ele digite a opção 4- Sair.
- Caso o cliente digite uma opção que não exista informe "Opção invalida".
- Algoritmo deve operar as quatro funções do caixa eletrônico.
- O Saldo inicial é igual a 0,00.
- Caso o usuário tente sacar um valor maior que o saldo disponível o programa deve apresentar a mensagem "Saldo insuficiente".
- No final de cada operação o saldo deve ser apresentado.
"""

saldo = 0.00

opcao = int(input("Escolha sua opção: 1 - Saldo \n 2 - Saque \n 3 - Depósito \n 4 - Sair\n"))

while opcao != 4:
    
    if opcao == 1:
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 2:
        valor_saque = float(input("Valor do saque: R$ "))
        
        if valor_saque > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= valor_saque
        
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == 3:
        valor_deposito = float(input("Valor Depósito: R$ "))
        saldo += valor_deposito
        print(f"Saldo atual: R$ {saldo:.2f}")

    else:
        print("Opção invalida")

    opcao = int(input("\nEscolha sua opção: 1 - Saldo \n 2 - Saque \n 3 - Depósito \n 4 - Sair\n"))

print("Saindo...")




      