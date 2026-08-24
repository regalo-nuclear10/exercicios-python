from random import randint
from time import sleep
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
print('PEDRA...')
sleep(1)
print('PAPEL...')
sleep(1)
print('TESOURA!!!')
print('==' * 12)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('==' * 12)

if jogador == 0:
	 if computador == 0:
	 	print('\033[35mEMPATE!\033[m')
	 elif computador == 1:
	 	print('\033[31mComputador venceu!\033[m')
	 elif computador == 2:
	 	print('\033[32mJogador venceu!\033[m')
elif jogador == 1:
	if computador == 0:
		print('\033[32mJogador venceu!\033[m')
	elif computador == 1:
		print('\033[35mEMPATE\033[m')
	elif computador == 2:
		print('\033[31mComputador venceu!\033[32m')
	else:
		print('JOGADA INVÁLIDA!')
elif jogador == 2:
	if computador == 0:
		print('\033[31mComputador venceu!\033[m')
	elif computador == 1:
		print('\033[32mJogador venceu!\033[m')
	elif computador == 2:
		print('\033[35mEMPATE!\033[m')
else:
	print('JOGADA INVÁLIDA')
