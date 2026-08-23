print('-' * 32)
print(f'{'Sequência de Fibonacci':^32}')
print('-' * 32)
Fibonacci = int(input('Quamtos números da sequência de Fibonacci deseja ver? '))
C = 2
N1 = 0
N2 = 1
print(f'{N1} > {N2}', end=' > ')
while C < Fibonacci:
	N3 = N1 + N2
	print(N3, end=' > ')
	N1 = N2
	N2 = N3
	C += 1
print('Acabou')