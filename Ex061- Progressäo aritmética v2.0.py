print('Gerador de PA')
print('==' * 15)
Primeiro = int(input('Primeiro termo: '))
Razão = int(input('Razão: '))
c = 0
while c < 10:
	print(Primeiro, end= ' > ')
	Primeiro += Razão
	c += 1
print('Acabou')
