total = maior1000 = 0
while True:
	nome_produto = str(input('Nome do produto: ')).strip().title()
	preço_produto = float(input('Preço do produto R$'))
	if preço_produto >= 1000:
		maior1000 += 1
		
	if total == 0 or preço_produto < preço_mais_barato:
		mais_barato = nome_produto
		preço_mais_barato = preço_produto
		
	total += preço_produto
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
	if resp == 'N':
		print('==' * 15)
		break
print(f'''Total gasto: R${total:.2f}
Total de Produtos acima de R$1000: {maior1000}
O produto mais barato foi {mais_barato}, custando R${preço_mais_barato:.2f}''')
