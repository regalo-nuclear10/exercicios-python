salário = float(input(' Seu salário: R$'))
print(f' O seu salário é de {salário:.2f}')
if salário <= 1250:
	N_salário = salário + (salário * 15 / 100)
	print(f' Com o aumento de 15% o seu salário passa para R${N_salário:.2f}')
else:	
	N_salário = salário + (salário * 10 / 100)
	print(f' Com o aumento de 10% o seu salário passa para R${N_salário:.2f}')