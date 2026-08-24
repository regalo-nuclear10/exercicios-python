n = 1
Soma = 0
Total = 0
while n != 999:
	n = int(input('Digite um número: '))
	if n != 999:
		Total += 1
		Soma += n
print(f'Ao todo foram digitados {Total} números e a sua soma é {Soma}'
)