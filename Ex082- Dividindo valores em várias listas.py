lista = []
pares = list()
impares = list()
while True:
	num = int(input('Digite um valor: '))
	lista.append(num)
	if num % 2 == 0:
		pares.append(num)
	else:
		impares.append(num)
	resp = str(input('Deseja comtinuar [S/N]: ')).strip().upper()
	if resp == 'N':
		break
print('==' * 20)
print(f'''Lista completa: {lista}
Lista de pares: {pares}
Lista de ímpares: {impares}''')
