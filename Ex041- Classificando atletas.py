from datetime import date
print('=' * 30)
print(f'{ "Confederaçäo de Natação":^30}')
print('=' * 30)
nasc = int(input('Seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
limpa = '\033[m'
print(f' Quem nasceu em {nasc} tem {idade} anos de idade')

if idade <= 9:
	print(f' Sua classificação é \033[35mMIRIM{limpa}')
	
elif idade <= 14:
	print(f' Sua classifcação é \033[32mINFANTIL{limpa}')
	
elif idade <= 19:
	print(f' Sua classificação é \033[34;42mJÚNIOR{limpa}')

elif idade <= 25:
	print(f' Sua classificação é \033[36m SÊNIOR{limpa}')
	
else:
	print(f' Sua classificação é \033[31mMASTER{limpa}')
