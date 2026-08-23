produtos = ('Lápis', 100, 'Borraha', 50,'Wiko Y87',70000,'Bolacha', 150, 'saldo', 500)
print('==' * 19)
print(f'{"Lista de preços":^38}')
print('==' * 19)
#cont = 0
#for mercadoria in produtos:
#	if cont % 2 == 0:
#		print(f'{mercadoria:.<30}',end=' ')
#	else:
#		print(f'{mercadoria}Kz')
#	cont += 1
#print('==' * 19)
for pos in range(len(produtos)):
	if pos % 2 == 0:
		print(f'{produtos[pos]:.<30}', end=' ')
	else:
		print(f'{produtos[pos]}Kz')
print('==' * 19)
