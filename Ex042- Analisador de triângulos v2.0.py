r1 = float(input(' Comprimento da primeira recta: '))
r2 = float(input(' Comprimento da segunda recta: '))
r3 = float(input(' Comprimento da terceira recta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
		print(' Os valores podem formar um triângulo', end = ' ')
		if r1 == r2 == r3:
			print('equilátero.')
		elif r1 != r2 != r3 != r1:
			print('escaleno.')
		else:
			print('isósceles')
else:
	print(' Os valores não formam um triângulo.')
	