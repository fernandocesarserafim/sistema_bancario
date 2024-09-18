import sys
import time
menu = """

Digite a opção desejada:

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

    print("="*50)
    menu_centralizado = " MENU "
    print(menu_centralizado.center(50," "))
    print("="*50)

    opcao = input(menu)

    if opcao in "dD":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Opearção falhou! O valor informado é inválido.")
    
    elif opcao in "sS":
        valor = float (input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")   

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saques: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao in "eE":
        print("\n=================== EXTRATO ===================")
        print("Não forma realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================")

    elif opcao in "qQ":
        print(f"Obrigado por utilizar nosso sistema.\nSaindo...")
        time.sleep(2)
        print("Programa finalizado com suceso!")
        sys.exit(0)

    else:("Operação inválida, por favor selecione novamente a operação desejada")