from datetime import date
Sexo = str(input('Seu sexo[M/F]: '))
if Sexo == 'F' or Sexo == 'f':
	print('Não é preciso te alistares!')
	
elif Sexo == 'M' or Sexo == 'm':
	nasc = int(input('Seu ano de nascimento:\033[32m'))
	print('\033[m')
	ano = date.today().year
	idade = ano - nasc

	if idade < 18:
		print(f'''Quem nasceu em {nasc} tem {idade} anos em {ano}
		O seu alistamento será daqui há {18 -idade} anos
		E terá q se alistar no ano de {nasc + 18}''')
	
	elif idade ==18:
		print('\033[31mÉ hora de se alistar! Estamos à tua espera soldado!\033[m')
	else:
		print(f'''\033[33mQuem nasceu em {nasc} tem {idade} anos
		Deveria ter se alistado há {idade - 18} anos
		E o seu alistamento foi em {nasc + 18} \033[m''')