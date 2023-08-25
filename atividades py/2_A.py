num_funcionarios = int(input("quantos funcionários existem na empresa? "))
funcionarios = []

for i in range(num_funcionarios):
    salario_inicial = float(input("digite o salário do funcionário {}: ".format(i + 1)))

    
    aumento = salario_inicial * 0.15
    salario_com_aumento = salario_inicial + aumento

    
    impostos = salario_com_aumento * 0.08
    salario_final = salario_com_aumento - impostos

    funcionario = {
        "numero": i + 1,
        "salario_inicial": salario_inicial,
        "salario_com_aumento": salario_com_aumento,
        "salario_final": salario_final
    }
    funcionarios.append(funcionario)


for funcionario in funcionarios:
    print("\nfuncionário {}: ".format(funcionario["numero"]))
    print("salário inicial: R$ {:.2f}".format(funcionario["salario_inicial"]))
    print("salário com aumento: R$ {:.2f}".format(funcionario["salario_com_aumento"]))
    print("salário final após desconto de impostos: R$ {:.2f}".format(funcionario["salario_final"]))
