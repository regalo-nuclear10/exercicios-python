from datetime import date
ano = date.today().year
Maior = 0
Menor = 0
for c in range(1, 8):
	print(f'{c}° Pessoa.')
	nasc = int(input('Digite seu ano de nascimento: '))
	if ano - nasc >= 21:
		Maior += 1
	else:
		Menor += 1
print(f'Das {c} pessoas, {Maior} são maiores de idade e {Menor} são menores')
