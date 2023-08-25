quantidade_de_frangos = int(input("Digite a quantidade de frangos: "))
pe_direito = quantidade_de_frangos * 4
pe_esquerdo = quantidade_de_frangos * (3.50*2)
valor_do_frango = pe_direito + pe_esquerdo
print("O valor para:",quantidade_de_frangos,"Frango(s) é de ",valor_do_frango,"Reais")