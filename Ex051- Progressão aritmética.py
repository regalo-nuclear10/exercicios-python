primeiro = int(input('Escolha um número para o começo da progressão: '))
razão = int(input('Escolha a razão da PA: '))
#for c in range (0, 10):
#	print(num,end =' ')
#	num = num + r
décimo = primeiro + 10 * razão
for c in range(primeiro, décimo, razão):
	print(c, end =' > ')
print('ACABOU!')
