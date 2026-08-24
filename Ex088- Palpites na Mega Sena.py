from random import sample
from time import sleep
print(f'{" Joga na MEGA SENA ":=^32}')
jogos = []
quant = int(input('Quantos jogos devo sortear? '))

for cont in range(quant):
	temp = (sample(range(1, 61), 6))
	temp.sort()
	jogos.append(temp[:])
	temp.clear()

print('==' * 3,f'Sorteando {quant:02} jogos', '==' * 3)	
for num, jogo in enumerate(jogos, start=1):
	print(f'Jogo {num}: {jogo}')
	sleep(1)
print('==' * 5,'Boa sorte!', '==' * 5)