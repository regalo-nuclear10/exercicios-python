lista= list(int(input(f'Digite o {_}° número: ' ))for _ in range(1, 6)) 
maior = menor = lista[0]
for valor in lista:
	if valor > maior:
		maior = valor
	if valor < menor:
		menor = valor
print(f'O maior número foi o {maior} nas posições:', end=' ')
for pos, num in enumerate(lista, start = 1):
	if num == maior:
		print(f'{pos}...', end=' ')
print()
print(f'O menor número foi o {menor} nas posições:', end=' ')
for pos, num in enumerate(lista, start = 1):
	if num == menor:
		print(f'{pos}...', end=' ')
print()
