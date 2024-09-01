menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair


=> """

saldo = 0
limite = 500
extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Déposito: R$ {valor:.2f}\n"

        else:
            print("Operação Falhou!\nPor favor, Informe um valor válido.")
            

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("O valor do saque excedeu o saldo disponível.")
        
        elif excedeu_limite:
            print("O valor de saque excedeu o valor limite de saques.")

        elif excedeu_saques:
            print("O limite de saques diários foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! Por favor informe um valor válido.")


    elif opcao == "3":
        print("\n========== Extrato ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione uma opcão válida")