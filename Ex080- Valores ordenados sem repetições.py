import os, time
lista = list()
#for c in range(5):
#	n = int(input('Digite um valor: '))
#	if c == 0 or n > lista[-1]:
#		lista.append(n)
#		print('Adicionado ao final da lista...')
#	else:
#		pos = 0
#		while pos < len(lista):
#			if n <= lista[pos]:
#				lista.insert(pos, n)
#				print(f'Adicionado na posição {pos}')
#				break
#			pos += 1
#time.sleep(2)
#os.system('clear')
#print(f'Os valores digitados em ordem foram: {lista}')
for c in range(5):
	num = int(input('Digite um valor: '))
	if c == 0 or num > lista[-1]:
		lista.append(num)
		print(f'Adicionado no fim da lista...')
	else:
		for pos in range(len(lista)):
			if num <= lista[pos]:
				lista.insert(pos, num)
				print(f'Adicionado na posição {pos}...')
				break
time.sleep(2)
os.system('clear')
print(f'Os valores digitados em ordem foram {lista}')