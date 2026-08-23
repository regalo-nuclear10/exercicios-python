from time import sleep
from os import system

lista = list()
maiorPeso = menorPeso = 0
maisLeve = list()
maisPesado = list()
while True:
	nome = str(input('Nome: '))
	peso = float(input('Peso: '))
	
	if len(lista) == 0:
		maiorPeso = menorPeso = peso
	else:
		if peso > maiorPeso:
			maiorPeso = peso
		if peso < menorPeso:
			menorPeso = peso
			
	lista.append([nome, peso])
	resp = str(input('Deseja continuar? [S/N]: '))
	if resp in 'Nn':
		break	
sleep(2)
system('clear')
print(f'Ao todo foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso registrado foi de {maiorPeso}Kg. Peso de', end=' ')
for pessoa in lista:
	if pessoa[1] == maiorPeso:
		print(f'[{pessoa[0]}]', end=' ')
print()
print(f'O menor peso registrado foi de {menorPeso}Kg. Peso de', end=' ')
for pessoa in lista:
	if pessoa[1] == menorPeso:
		print(f'[{pessoa[0]}]')
