# Resolução do desafio "Criando um Sistema Bancário com Python", do Bootcamp "Santander 2025 - Back-End com Python".

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        deposito = int(input("Quanto deseja depositar? "))
        
        if deposito > 0:
            saldo = saldo + deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito} realizado com sucesso!")
        else:
            print("Digite apenas valores positivos.")
            deposito = input("Tente novamente. Quanto deseja depositar? ")


    elif opcao == "s":
        saque = int(input("Quanto deseja sacar?"))
        if saldo > saque and saque <= 500:
            saldo = saldo - saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso. Seu novo saldo é R$ {saldo}")
        elif saldo < saque:
            print("Você não tem saldo suficiente!")
        elif saque > 500:
            print("O limite por saque é R$ 500,00. Tente outro valor.")
        elif numero_saques == 3:
            print("Número máximo de saques excedido!")
        else:
            print("Operação falhou. Valor inválido.")


    elif opcao == "e":
        print("\n************* EXTRATO *************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n***********************************")
        
    elif opcao == "q":
        break
    else:
        print("Operação inválida. Por favor, selecione novamente a opção desejada")










