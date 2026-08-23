from random import randint
números = tuple(randint(0, 20) for _ in range(5))
print('Os números sorteados foram:',end = ' ')
maior_núm = números[0]
menor_núm = números[0]
for c in números:
	print(c, end = ' ')
	if c > maior_núm:
		maior_núm = c
	else:
		if c < menor_núm:
			menor_núm = c
print(f'\nO maior número sorteado foi: {maior_núm}')
print(f'O menor número sorteado foi: {menor_núm}')