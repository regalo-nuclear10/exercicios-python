from time import sleep
from random import randint
vitória = 0
print('\033[36mVamos jogar par ou ímpar\033[m')
print('=-' * 15)

while True:
	núm_jogado = int(input('Diga um valor: '))
	player_choose = str(input('Par ou ímpar [P/I]: ')).upper().strip()[0]
	núm_computador = randint(0, 10)
	resultado = núm_jogado + núm_computador
	while player_choose not in 'PI':
		player_choose = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
	if player_choose == 'P': 
		if resultado% 2 == 0:
			print('=-' * 15)
			print(f'Vc escolheu {núm_jogado} e computador escolheu {núm_computador}, resultado é {núm_jogado + núm_computador}.\033[32mDeu PAR!\033[m')
			vitória += 1
			print('Vc venceu, vamos outra vez...')
		else:
			print(f'Vc escolheu {núm_jogado} e computador escolheu {núm_computador}, resultado é {núm_jogado + núm_computador}.\033[31mDeu Ímpar!\033[m')
			sleep(1)
			break
	if player_choose == 'I':
		if resultado % 2 == 1:
			print(f'Vc escolheu {núm_jogado} e computador escolheu {núm_computador}, resultado é {núm_jogado + núm_computador}.\033[32mDeu Ímpar\033[m')
			vitória += 1
			print('Você venceu....Mais uma vez...')	
		else:
			print(f'Vc escolheu {núm_jogado} e computador escolheu {núm_computador}, o resultado é {resultado}.\033[31mDeu Par! Você perdeu\033[m')
			sleep(1)
			break
			
if vitória == 1:
	print(f'Jogo acabou...Você venceu {vitória} vez!')
elif vitória > 1:
	print(f'Jogo acabou...Você venceu {vitória} vezes!')	
elif vitória == 0:
	print('Vc ñ venceu nenhuma vez')
