from os import  system
from time import sleep
matriz = [[] , [], []]
cont = 1
somaPar = soma_coluna3 = maior_linha2 = 0
for linha in range(3):
	for coluna in range(3):
		matriz[linha].append(int(input(f'Digite o {cont}° de 9 números: ')))
		if matriz[linha][coluna] % 2 == 0:
			somaPar += matriz[linha][coluna]
		if coluna == 2:
			soma_coluna3 += matriz[linha][coluna]
		if linha == 1:
			if len(matriz[linha]) <= 1 or  matriz[linha][coluna] > maior_linha2:
				maior_linha2 = matriz[linha][coluna]
		cont += 1

sleep(1)
system('clear')
for linha in range(3):
	for coluna in range(3):
		print(f'[{matriz[linha][coluna]:^5}]', end=' ')
	print()

print('==' * 30)
print(f'A soma dos pares digitados é: {somaPar}')
print(f'A soma dos elementos da terceira coluna é: {soma_coluna3}')
print(f'E o maior valor da segunda linha é: {maior_linha2}')
