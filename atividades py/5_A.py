print("Bem-vindo ao Banco Orixi - Abertura de Conta Poupança\n")

deposito_inicial = float(input("Informe o valor do depósito inicial: R$ "))
taxa_juros = float(input("Informe a taxa de juros (em %): ")) / 100
meses = int(input("Informe a quantidade de meses que pretende investir: "))

saldo = deposito_inicial
total_juros = 0

for mes in range(1, meses + 1):
    print("\nMês", mes)
    
    depositar = input("Deseja fazer um depósito neste mês? (s/n): ")
    if depositar == "s":
        valor_deposito = float(input("Informe o valor do depósito: R$ "))
        saldo += valor_deposito
    
    juros_mes = saldo * taxa_juros
    saldo += juros_mes
    total_juros += juros_mes
    
    print("Saldo atual: R$ {:.2f}".format(saldo))

print("\nTotal ganho com juros no período: R$ {:.2f}".format(total_juros))
print("Saldo final após investimento: R$ {:.2f}".format(saldo))

