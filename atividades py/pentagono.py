import numpy as np
lados= int(input("digite o numemro de lados: "))
x_l = []
y_l = []

for i in range(1,lados+1):
    x = float(input("entra com o valor de x "+str(i)))
    y = float(input("entre com o valor de y "+str(i)))
    x_l.append(x)
    y_l.append(y)

print(x_l)
print(y_l)

area = 0
for i in range(lados):
    print(i, i+1)
    if(i!=lados-1):
        area += (x_l[i]*y_l[i+1]) - (x_l[i+1]*y_l[i]) 
    else:   
        area += (x_l[i]*y_l[0]) - (x_l[0]*y_l[i])
    
    
area = np.abs(area)*0.5
print("area = "+str(area))

localidade = str(input("onde fica localizado o terreno? "))
while(True):
    if localidade == "centro":
        print("valor do metro quadrado R$: ",area*130)
    if localidade == "areanobre":
        print("valor do metro quadrado R$: ",area*200)
    if localidade == "periferia":
        print("valor do metro quadrado R$: ",area*80)
    else:
        print("voce digitou uma opção invalida!")