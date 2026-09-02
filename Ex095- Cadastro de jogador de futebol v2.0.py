from time import sleep
from rich import print
from os import system
from rich.console import Console
from rich.table import Table

equipa = list()
jogador = dict()
	
while True:
	jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
	
	while True:
		try:
			jogos = int(input(f'Quantos jogos {jogador['nome']} jogou? '))
			if jogos < 0:
				raise ValueError()
		except ValueError:
			print('[red]Erro! Não foi digitado um número válido[/red]')
			sleep(1)
			continue
		break
	
	while True:
		try:	
			jogador['golos'] = list(int(input(f'Golos de {jogador['nome']} na {_ + 1}ª partida: '))for _ in range(jogos))
		except ValueError:
			print('[red]ERRO! Inserção de dados incorrecta[/red]')
			sleep(1)
			continue
		break
		
	jogador['total de golos'] = sum(jogador['golos'])
	equipa.append(jogador.copy())
	while True:
		try:
			resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
			if resp in ('S', 'N'):
				system('clear')
				break
			else:
				print('Digite apenas [green]S[/] ou [red]N[/]')
				sleep(2)
		except IndexError:
			print('[red]Mensagem vazia[/]')
			sleep(2)
	if resp == 'N':
				break
	
table = Table()
table.add_column('Código', justify='left')
table.add_column('Nome', justify='left')
table.add_column('Golos', justify='center')
table.add_column('Total', justify='right')

for pos, player in enumerate(equipa):
	table.add_row(f'{pos}', f'{player['nome']}',f'{player['golos']}', f'{player['total de golos']}')
	
console = Console()
console.print(table)
while True:
	while True:
		try:
			print('=+=' * 10)
			cod = int(input('Digite o código do jogador para ver os detalhes(999 interrompe):'))
			if cod == 999:
				break
			player = equipa[cod]
			print(f'Mostrando detalhes do jogador [green]{player['nome']}[/green]...')
		except ValueError:
			print('[red]Erro! Não foi digitado um número[/red]')
			continue
		except (IndexError,TypeError):
			print(f'Não existe jogador com o código [red]{cod}[/red]')
			continue

		print(f'Teve um total de {len(player["golos"])} partidas')
		for p, g in enumerate(player['golos'], start=1):
			print(f'\t=> Na {p}ª fez {g} golos.')
			sleep(0.7)
		sleep(3)
		system('clear')
		console.print(table)
	break
print('<Volte sempre>')
