from time import sleep
jogador = dict()
jogador['nome'] = str(input('Nome do jogador: ')).title()
jogos = int(input(f'Quantos jogos {jogador['nome']} jogou? '))
jogador['golos'] = list(int(input(f'Golos de {jogador['nome']} na {_ + 1}ª partida: '))for _ in range(jogos))
jogador['total de golos'] = sum(jogador['golos'])
print('==' * 20)
print(jogador)
sleep(0.7)
print('==' * 20)
for k, v in jogador.items():
	print(f'O campo {k} tem o valor {v}')
	sleep(0.7)
print('==' * 20)
print(f'O jogador {jogador['nome']} fez {jogos} partidas.')
for p, v in enumerate(jogador['golos'], start=1):
	print(f'\t=>Na {p}ª partida fez {v} golos.')
	sleep(0.7)
print(f'{jogador['nome']} fez um total de {jogador['total de golos']} golos.')

