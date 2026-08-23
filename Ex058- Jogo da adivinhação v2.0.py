import os, time
from random import randint
from time import sleep
tentativa = 0
jogador = -1
print("""Sou seu computador...
Pensei em um número entre 0 e10.""")
computador = randint(0, 10)
while jogador != computador:
	jogador = int(input('Qual é o seu palpite? '))
	tentativa += 1
	sleep(0.5)
	if jogador < computador:
		print('Muito baixo....Tente novamente')
		time.sleep(2)
		os.system('clear')
	elif jogador > computador:
		print('Muito alto...Tente novamente')
		time.sleep(2)
		os.system('clear')	
print(f'Você venceu em {tentativa} tentativas!')
