from datetime import datetime
import pytz
import textwrap

def menu():
    menu = """

    Menu

    [1] Depositar
    [2] Saque
    [3] Extrato
    [4] Novo Usuário
    [5] Nova Conta
    [6] Listar Contas
    [7] Sair


    => """
    return input(textwrap.dedent(menu))

data = datetime.now(pytz.timezone("America/Sao_Paulo"))
mascara_ptbr = "%d/%m/%y %H:%M"

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor informado é inválido")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, quantidade_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = quantidade_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente.")
    
    elif excedeu_limite:
        print("Valor de saque excedeu o limite.")

    elif excedeu_saques:
        print("Número de saques diários excedido.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f} | {data.strftime(mascara_ptbr)}\n"
        quantidade_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Valor informado é inválido!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("============ EXTRATO ============")
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário cadastrado com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd-mm-aaaa): ")
    endereco = input("Infome o seu endereço (Logradouro, nro - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, por favor tente novamente.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
"""
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    quantidade_saques = 0
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()
        
        if opcao == ("1"):
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == ("2"):
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                quantidade_saques=quantidade_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == ("3"):
            exibir_extrato(saldo, extrato=extrato)


        elif opcao == ("4"):
           criar_usuario(usuarios)

        elif opcao == ("5"):
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == ("6"):
            listar_contas(contas)

        elif opcao == ("7"):
            break

        else:
            print("Por favor, selecione uma opção válida")
main()
