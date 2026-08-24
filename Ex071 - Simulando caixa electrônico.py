from time import sleep
cédula = 50
tot_cédula = 0
print('~~~~' * 7)
print(f'{'Banco Regalo':^27}')
print('~~~~' * 7)
while True:
	valor = int(input('Valor a sacar: '))
	print('==' * 14)
	print(f'Para R${valor} serão: ')
	while True:
		if valor >= cédula:
			valor -= cédula
			tot_cédula += 1
		else:
			if tot_cédula > 0:
				print(f' {tot_cédula} cédulas de {cédula}')
				tot_cédula = 0
			if cédula == 50:
				cédula = 20
			elif cédula == 20:
				cédula = 10
			elif cédula == 10:
				cédula = 1
			elif valor == 0:
				break
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
		print('==' * 14)
	if resp == 'N':
		print('Fechando...')
		sleep(1.6)
		break
print('Obrigado por escolher o Banco Regalo')
