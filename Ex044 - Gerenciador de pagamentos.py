preço = float(input('Preço do produto: '))
print('''Condição de pagamento:
	1. À vista no dinheiro/cheque
	2. À vista no cartão
	3. Parcelado no cartão''')
print('=' * 20)
condição = int(input('Opção:'))

if condição == 1:
	Novo_valor = preço - (preço *10) /100
	print(f'O produto vai ter 10% de desconto, com um valor original de R${preço} e o novo valor de R${Novo_valor:.2f}')
elif condição == 2:
	Novo_valor = preço - preço * 5 / 100
	print(f'O produto vai ter 5% de desconto, com um valor original de R${preço} e o novo valor de R${Novo_valor:.2f}')
elif condição == 3:
	tot_parcela = int(input('Vai parcelar quantas vezes? '))
	if tot_parcela <= 2:
		parcela = preço / tot_parcela
		print(f'O preço do produto parcelado em {tot_parcela} vezes vai ser R${parcela} e no final vai custar R${preço}')
	elif tot_parcela >= 3:
		Novo_valor = preço + preço * 20 /100
		parcela = Novo_valor / tot_parcela
		print(f'O produto vai ter 20% de juros, com um valor original de R${preço} e parcelado {tot_parcela} vezes de R${parcela}, no final vai custar R${Novo_valor:.2f}')
		