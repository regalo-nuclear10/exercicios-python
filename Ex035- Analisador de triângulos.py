r1 = float(input(' Comprimento da prmeira recta: '))
r2 = float(input(' Comprimento da segunda recta: '))
r3 = float(input(' Comprimento da terceira recta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print(' Esses valores formam um triângulo!')
else:
	print(' Esses valores não formam um triângulo!')