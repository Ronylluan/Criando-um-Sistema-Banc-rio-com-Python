# Importando o módulo datetime para trabalhar com datas e horas
import datetime

# Variáveis globais para armazenar saldo, limite, extrato e número de saques
SALDO = 0.0
LIMITE = 500.0
EXTRATO = []
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3
DATA_ULTIMO_SAQUE = None

def depositar(valor):
    """
    Realiza um depósito na conta bancária.
    
    Parâmetros:
    valor (float): Valor a ser depositado, deve ser positivo.
    """
    global SALDO
    if valor > 0:
        SALDO += valor
        EXTRATO.append({"tipo": "Depósito", "valor": valor, "data": datetime.datetime.now()})
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")

def sacar(valor):
    """
    Realiza um saque na conta bancária, respeitando os limites diários e de saldo.
    
    Parâmetros:
    valor (float): Valor a ser sacado.
    """
    global SALDO, NUMERO_SAQUES, DATA_ULTIMO_SAQUE

    hoje = datetime.date.today()

    # Verifica se é um novo dia para resetar o contador de saques diários
    if DATA_ULTIMO_SAQUE != hoje:
        NUMERO_SAQUES = 0
        DATA_ULTIMO_SAQUE = hoje
    
    if valor <= 0:
        print("O valor do saque deve ser positivo.")
    elif NUMERO_SAQUES >= LIMITE_SAQUES:
        print("Limite diário de 3 saques atingido.")
    elif valor > LIMITE:
        print("O limite máximo por saque é de R$ 500,00.")
    elif valor > SALDO:
        print("Saldo insuficiente.")
    else:
        SALDO -= valor
        NUMERO_SAQUES += 1
        EXTRATO.append({"tipo": "Saque", "valor": -valor, "data": datetime.datetime.now()})
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

def exibir_extrato():
    """
    Exibe o extrato bancário, listando todos os depósitos e saques realizados.
    """
    print("\nExtrato Bancário:")
    if not EXTRATO:
        print("Não há transações para exibir.")
    else:
        for transacao in EXTRATO:
            data = transacao["data"].strftime("%Y-%m-%d %H:%M:%S")
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f"{data} - {tipo}: R$ {valor:.2f}")
    
    print(f"Saldo Atual: R$ {SALDO:.2f}\n")

# Menu de opções
menu = '''
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[0] SAIR

=> '''

while True:
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))
        depositar(valor_deposito)

    elif opcao == "2":
        valor_saque = float(input("Informe o valor do saque: "))
        sacar(valor_saque)

    elif opcao == "3":
        exibir_extrato()

    elif opcao == "0":
        print("Saindo ... Tenha um Bom Dia! ")
        break

    else: 
        print("Operação inválida!!! Selecione uma opção válida do menu.")
