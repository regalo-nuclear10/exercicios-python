Soma = 0
Total = 0
while True:
	n = int(input('Digite um número(999 para parar): '))
	if n == 999:
		break
	Soma += n
	Total += 1
print(f'A soma dos {Total} valores é {Soma}!')
