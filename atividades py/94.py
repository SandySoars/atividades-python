galeris = list ()
pessoa = dict()
while True:
    pessoa ['nome'] = str(input("Digite seu nome "))
    while True:
        pessoa ['sexo'] =  str(input("qual seu sexo? [F/M] ")).upper()[0]
        if pessoa ['sexo'] in 'F/M':
            break
        print("erro! digite apenas F ou M ")
    pessoa ['idade'] = int(input("digite sua idade "))
    try:
        pessoa ['cpf'] = int(input("digite seu cpf: "))
    except:
        print("erro! cpf invalido! ")
    while True:
        resp = str(input("quer continuar [S/N] ")).upper()[0]
        if resp in 'S/N':
            break 
        print("erro!apenas S ou N ")
    break 
print(pessoa)
