primeiro = float(input("quantos metros? "))
segundo = float(input("quantos metros? "))
terceiro = float(input("quantos metros? "))
quarto= float(input("quantos metros? "))
quinto= float(input("quantos metros? "))

a = (primeiro + segundo) / 2 
b = (terceiro + quarto) / 2
m_quadrados = a * b 
print("metros quadrados: ", m_quadrados)

localidade = str(input("onde fica localizado o terreno? "))

if localidade == "centro":
    print("valor do metro quadrado R$: ",m_quadrados*130)
if localidade == "areanobre":
    print("valor do metro quadrado R$: ",m_quadrados*200)
if localidade == "periferia":
    print("valor do metro quadrado R$: ",m_quadrados*80)