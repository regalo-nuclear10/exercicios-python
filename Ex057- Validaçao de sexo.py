sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()

while sexo not in 'MF':
	print('Digite um sexo válido!')
	sexo = str(input('Digite o seu sexo[M/F]: ')).upper().strip()
if sexo[0] == 'M':
	print('Registrado um indivíduo do sexo masculino')
else:
	print('Registrado um indivíduo do sexo feminino')
	