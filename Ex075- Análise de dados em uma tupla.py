tupla = tuple(int(input('digite um número: ')) for _ in range(4))
print(f'O número 9 apareceu {tupla.count(9)} vezes')
for pos, núm in enumerate(tupla, start = 1):
	if núm == 3:
		print(f'O número 3 aparece pela primeira vez na posição {pos}')
if tupla.count(3) == 0:
	print('O número 3 não aparece nenhuma vez!')
if any(núm % 2 == 0 for _ in tupla):
 	print('Os números pares digitados foram:', end=' ')
 	for núm in tupla:
 		if núm % 2 == 0:
 			print(núm, end=' ')
else:
	print('Não há números pares')
