salario = float(input("Digite o salário R$: "))
print("O salario atual é: ",salario)
aumento = salario * 0.15
print("O salario com aumento de 15% é R$:",aumento)
salario_com_aumento = salario + aumento
desconto = salario_com_aumento * 0.08
salario_final = salario_com_aumento - desconto
print("O salário final após o aumento e desconto é R$:", salario_final)