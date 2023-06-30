saldo = 1000.00

qnt_saque = 0
qnt_deposito = 0

depositos = []
depositos2 = []

saques = []
saques2 = []

menu = "s - Sacar\nd - Depositar\ne - Extrato\nq - Sair\nDigite a letra da opcao desejada: "

opcao = input(menu)

while True:

    if opcao == "s":
        if qnt_saque == 3:
            print("\nApenas sao permitidos 3 saques por dia\n")
            opcao = input(menu)

        elif qnt_saque < 3:
           saque = float(input("Quanto deseja sacar? "))
           
           if saque > saldo:
              print("\nSaldo indisponivel\n")
              opcao = input(menu)
           elif saque > 500.00:
              print("\nApenas são permitidos saques de no maximo R$ 500.00\n")
           else:
              print("\nSaque feito com sucesso!\n")
              qnt_saque += 1
              saldo -= saque
        
              saques.append(saque)
              saques2 = ["R$" + str(saque) for saque in saques]

              opcao = input(menu)

    elif opcao == "d":
        deposito = float(input("Quanto deseja depositar? "))

        if deposito <= 0:
            print("\nApenas é permitido deposito de valores positivos\n")
        else:
            print("\nDeposito feito com sucesso\n")
            qnt_deposito += 1
            saldo += deposito
            depositos.append(deposito)

            depositos2 = ["R$" + str(deposito) for deposito in depositos]

            opcao = input(menu)

    elif opcao == "e":
        print("\nEXTRATO")

        if qnt_saque == 0 & qnt_deposito == 0:
            print("Não foram realizadas movimentações")
            print(f"Saldo: {saldo}")
            print("\n")
            opcao = input(menu)
        else:
            print(f"Depositos feitos: {depositos2}")
            print(f"Saques feitos: {saques2}")
            print(f"Saldo: {saldo}")
            print("\n")
            opcao = input(menu)

    elif opcao == "q":
        break
    else:
        print("\nOpcao invalida\n")
        opcao = input(menu)
        
