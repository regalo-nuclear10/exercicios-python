S = 0
C = 0
for c in range(1, 7):
	n = int(input(f'Digite o {c}° número: '))
	if n % 2 == 0:
		S += n
		C += 1
print(f'A soma dos {C} números pares digitados é {S}')
