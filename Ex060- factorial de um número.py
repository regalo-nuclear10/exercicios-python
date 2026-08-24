num = int(input('Digite um número para ver seu factorial:  '))
factorial = 1
c = num
print(f'Calculando {num}! = ', end = '')
while c > 0:
	print(f'{c}', end = '')
	print(' x ' if c > 1 else ' = ', end = '')
	factorial  *= c
	c -= 1
print(f'{factorial}')
