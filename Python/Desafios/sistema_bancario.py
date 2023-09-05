import os
import platform

saldo = 100
valor_limite_saque = 500
extrato = ""
saques_realizados = 0
limite_saques = 3

menu = """
Selecione a operação que deseja realizar:

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

def limpar_terminal():
    sistema = platform.system()
    
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux" or sistema == "Darwin":
        os.system("clear")
    else:
        pass
    
def pause():
    input("\nPressione Enter para continuar...")
    limpar_terminal()

def mostrar_saldo():
    global saldo
    
    print(f"Saldo R$ {saldo:.2f}\n")


def sacar(valor):
    global saldo, saques_realizados, extrato
    
    if saques_realizados >= limite_saques:
        print("\nLimite de saques atingido. Não é possível realizar mais saques.")
    elif valor < 0:
        print("\nValor inválido. Não é possível sacar um valor negativo.")
    elif saldo >= valor and valor <= valor_limite_saque:
        extrato += f"Saldo R$ {saldo:.2f}\n"
        saldo -= valor
        saques_realizados += 1
        extrato += f"- R$ {valor:.2f}\n"
        print(f"\nSaque de R$ {valor:.2f} realizado!")
    elif valor > valor_limite_saque:
        print(f"\nO valor de saque (R$ {valor:.2f}) excede o limite disponível de R$ {valor_limite_saque:.2f}.")
    else:
        print("\nSaldo insuficiente para realizar o saque.\n")

def depositar(valor):
    global saldo, extrato
    
    if valor < 0:
        print("\nValor inválido. Não é possível depositar um valor negativo.")
    else:
        extrato += f"Saldo R$ {saldo:.2f}\n"
        saldo += valor
        extrato += f"+ R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado!")


limpar_terminal()


while True:    
    opcao_menu = input(menu)
    limpar_terminal()
    
    if opcao_menu == "d":
        print("\n------------------------- DEPÓSITO -------------------------\n")
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        depositar(valor_deposito)
        print("\n------------------------------------------------------------\n")
        pause()
        
    elif  opcao_menu == "s":
        print("\n-------------------------- SAQUE ---------------------------\n")
        valor_saque = float(input("Digite o valor do saque: R$ "))
        sacar(valor_saque)
        print("\n------------------------------------------------------------\n")
        pause()
        
    elif  opcao_menu == "e":
        print("\n========================= EXTRATO ==========================\n")
        print(extrato)
        mostrar_saldo()
        print("\n============================================================\n")
        pause()
        
    elif  opcao_menu == "q":
        print("\n- Sair\nEncerrando operações...")
        break
    
    else:
        print("\n============================================================\n")
        print("Operação Inválida! \nPor favor, selecione novamente a operação desejada.")
        print("\n============================================================\n")
        pause()

