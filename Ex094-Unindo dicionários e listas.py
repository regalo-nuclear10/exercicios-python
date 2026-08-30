from time import sleep
from os import system
from rich import print
pessoas = list()
dados = dict()
tot_idade = 0
mulheres = list()
acima_media = []
while True:
	dados['nome'] = str(input('Nome: ')).strip().title()
	while True:
		dados['idade'] = int(input('Idade: '))
		if dados['idade'] >= 0:
			tot_idade += dados['idade']
			break
		print('[red]ERRO! Idade inválida[/red].')
		sleep(1.5)
	while True:
		dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
		if dados['sexo'] in ('M','F'):
			break
		print('[red]ERRO! Digte apenas M ou F[/red].')
		sleep(1.5)
	pessoas.append(dados.copy())
	while True:
		resp = str(input('Deseja continuar? [S/N]: ')).strip().title()
		if resp in ('S','N'):
			system('clear')
			if resp == 'N' or resp == 'S':
				break
		else:
			print('[red]ERRO! Digite apenas S ou N[/red].')
			sleep(1.5)
	if resp == 'N':
		break
system('clear')
media_idade = tot_idade//len(pessoas)

print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade é de {media_idade} anos.')

for pessoa in pessoas:
	if pessoa['sexo'] == 'F':
		mulheres.append(pessoa['nome'])
	if pessoa['idade'] > media_idade:
		acima_media.append([pessoa['nome'], pessoa['idade']])
		
print(f'As mulheres são: {mulheres}')
print('As pessoas com idade acima da média são:')
for nome, idade in acima_media:
	print(f'nome={nome}; idade={idade}')
print('<Encerrado>')
