from time import sleep
from random import randint
jogo = {'jogador1' : randint(1, 6),'jogador2' : randint(1, 6), 'jogador3' : randint(1, 6), 'jogador4' : randint(1, 6)}
ranking = {}
print('== Valores sorteados ==')
for k, v in jogo.items():
	print(f' {k} tirou {v} no dado.')
	sleep(1)
print('== Ranking ===') 
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)
for i, p in enumerate(ranking, start=1):
	print(f' {i}° lugar: {p[0]} com {p[1]}.')
	sleep(1)