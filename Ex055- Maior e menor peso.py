MaiorP = 0
MenorP = 0
for c in range(1, 6):
	peso = float(input(f'Digite o peso da {c}° pessoa: '))
	if c == 1:
		MaiorP = peso
		MenorP = peso
	else:
		if peso > MaiorP:
			MaiorP = peso
		if peso < MenorP:
			MenorP = peso
print(f'O menor peso digitado foi {MenorP}Kg.')
print(f'O maior peso digitado foi {MaiorP}Kg.')