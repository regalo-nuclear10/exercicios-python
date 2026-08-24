from random import randint
import time
print('-=-' * 10)
print("""Vamos jogar um jogo, vou pensar em um número entre 0 e 5, e tens q adivinhar qual número pensei, vamos lá!.\n Já! Tenta adivinhar""")
print('-=-' * 10)
num = randint(0, 5)
n = int(input(' Qual número você acha que pensei? : \033[31m'))
print(' Processando...\033[m')
time.sleep(2)
if n == num:
	print('\033[34mParabéns, venceste!\033[m ')
else:
	print(f' É uma pena, mas eu venci kkkk \n Eu pensei no número \033[32m{num}\033[m!')
