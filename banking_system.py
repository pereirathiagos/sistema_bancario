# Menu de opções do sistema bancário
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>"""

# Inicialização das variáveis
saldo = 500   
limite = 500  
extrato = ""  
numero_saques = 0  
LIMITE_SAQUES = 3  # Limite máximo de saques por dia

# Loop principal do programa
while True:
    opcao = input(menu)  # Exibe o menu e recebe a opção do usuário

    # Opção 1: Depositar
    if opcao == "1":
        try:
            # Recebe o valor do depósito
            valor = float(input("Informe o valor do depósito: "))
            # Verifica se o valor é positivo
            if valor > 0:
                saldo += valor  # Atualiza o saldo
                extrato += f"Depósito: R$ {valor:.2f}\n"  # Adiciona ao extrato
            else:
                print("Operação falhou! Valor é inválido!")  # Valor negativo ou zero
        except ValueError:
            print("Operação falhou! Valor inválido!")  # Entrada não numérica

    # Opção 2: Sacar
    elif opcao == "2":
        try:
            # Recebe o valor do saque
            valor = float(input("Informe o valor do saque: "))
            # Verifica se o valor excede o saldo, o limite ou o número de saques
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            # Verifica as condições para o saque
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite da conta.")
            elif excedeu_saques:
                print("Operação falhou! Tentativas de saque excedem o limite diário!")
            elif valor > 0:
                saldo -= valor  # Atualiza o saldo
                extrato += f"Saque: R$ {valor:.2f}\n"  # Adiciona ao extrato
                numero_saques += 1  # Incrementa o número de saques realizados
            else:
                print("Operação falhou! O valor informado é inválido.")  # Valor negativo ou zero
        except ValueError:
            print("Operação falhou! Valor inválido.")  # Entrada não numérica

    # Opção 3: Exibir extrato
    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        # Exibe o extrato ou uma mensagem se não houver movimentações
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo atual
        print("===============================")

    # Opção 0: Sair do programa
    elif opcao == "0":
        break

    # Opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
