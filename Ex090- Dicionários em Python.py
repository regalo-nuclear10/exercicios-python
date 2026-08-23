from rich import print
aluno = dict()
nome = str(input('Nome:'))
aluno['nome'] = nome
while True:
	media = float(input(f'Média de {nome}:'))
	aluno['média'] = media
	if media >= 7:
		aluno['situação'] = '[green]aprovado[/green]'
	elif media >= 5:
		aluno['situação'] = '[yellow]em recuperação[/yellow]'
	elif media >= 0:
		aluno['situação'] = '[red]reprovado[/red]'
	elif media > 10 or media < 0:
		print('Essa média não é permitida(máx.10)')
		continue
	break

print('==' * 15)	
for k, v in aluno.items():
	print(f'{k} é {v}')
	