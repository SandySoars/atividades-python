deposito_inicial = float(input("Digite o valor do Depósito: "))
juros = float(input("Informe o valor do juros: "))
for i in range(1, 25):
    deposito_inicial = deposito_inicial + deposito_inicial * (juros / 100)
    print(f"Mês {i}: R${deposito_inicial:.2f}")
print("O valor total ganho com os juros = R$",())