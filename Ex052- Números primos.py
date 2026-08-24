num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
	if num % c ==0:
		print('\033[32m', end=' ')
		divisor = c
		tot += 1
		print(f'{divisor}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
	print('Por isso ele é PRIMO!')
elif tot == 1:
	print('Apesar do número 1 ser divisivel apenas por ele, ñ é considerado primo')
else:
	print('Por isso ele ñ é PRIMO!')