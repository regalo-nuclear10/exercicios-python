from datetime import date
from time import sleep
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
pessoa['Idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['CPTS'] = int(input('Carteira de trabalho(0 não tem): '))
if pessoa['CPTS'] != 0:
	pessoa['Contratação'] = int(input('Ano de contratação: '))
	pessoa['Salário'] = float(input('Salário: R$'))
	pessoa['Aposentadoria'] = pessoa['Idade'] + 	pessoa['Contratação'] + 35 - date.today().year
print('==' * 15)
for k, v in pessoa.items():
	print(f'{k} tem o valor {v}')
	sleep(0.5)