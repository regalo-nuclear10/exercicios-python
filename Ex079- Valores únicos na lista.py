from os import system
lista = list()
while True:
	num = int(input('Digite um número: '))
	if num in lista:
		print('Valor duplicado, não foi adicionado!')
	else:
		lista.append(num)
		print('Valor adicionado com sucesso!')
		
	Resp = str(input('Deseja continuar? [S/N]')).strip().upper()
	system('clear')
	if Resp == 'N':
		break
lista.sort()
print(f'Foram digitados os valores {lista}')
