num = int(input('Escolha um número para ver a sua tabuada: '))
print(f'A tabuada do número {num} é:')
print('=' * 15)
for c in range(1, 11):
	print(f'{num} x {c:02} = {num * c:02}')
print('=' * 15)
