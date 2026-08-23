import os, time
lista = list()
while True:
	lista.append(int(input('Digite um número: ')))
	resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
	if resp == 'N':
		break
time.sleep(2)
os.system('clear')
print(f'Ao total foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é a seguinte: {lista}')
if 5 in lista:
	print('O número 5 está na lista')
else:
	print('O número 5 não está na lista')
