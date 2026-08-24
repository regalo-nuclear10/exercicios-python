S = 0
Cont = 0
#for c in range(1 , 500):
#	if c % 2 == 1 and c % 3 == 0:
#		S = S + c
#		Cont = Cont + 1
for c in range(1, 500, 2):
	if c % 3 == 0:
		S += c
		Cont += 1
print(f'A soma dos {Cont} números impares múltiplos de 3 entre 1 e 500 é {S}')