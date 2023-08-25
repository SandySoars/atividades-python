frangos = float(input("quantos frangos? "))
tipo_racao = input("Digite o tipo de ração (A ou B): ")
peso_inicial = float(input("Digite o peso inicial médio dos frangos em quilos: "))
valor_venda_por_quilo = float(input("Digite o valor de venda por quilo de frango: "))
        
anel = 4
anel_alimento = 3.50

if tipo_racao == "A":
    aumento_porcentagem = 0.20
    custo_racao_por_quilo = 2.50
elif tipo_racao == "B":
    aumento_porcentagem = 0.14
    custo_racao_por_quilo = 3.00

peso_final = peso_inicial * (1 + aumento_porcentagem)
gasto_total_chip = frangos * anel
gasto_total_racao = (peso_final - peso_inicial) * custo_racao_por_quilo * frangos
gasto_total_alimento = frangos * 2 * anel_alimento

gasto_total = gasto_total_chip + gasto_total_racao + gasto_total_alimento
faturamento = peso_final * frangos * valor_venda_por_quilo

print(f"Gasto total da granja: R$ {gasto_total:.2f}")
print(f"Faturamento do fazendeiro: R$ {faturamento:.2f}")