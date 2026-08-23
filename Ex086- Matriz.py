from os import  system
from time import sleep
matriz = [[] , [], []]
cont = 1
for linha in range(3):
	for coluna in range(3):
		matriz[linha].append(int(input(f'Digite o {cont}° de 9 números: ')))
		cont += 1

sleep(1)
system('clear')
for linha in range(3):
	for coluna in range(3):
		print(f'[{matriz[linha][coluna]:^5}]', end=' ')
	print()
