numeros = [ [], []]
for cont in range(1, 8):
	num = int(input(f'Digite o {cont}° de 7 números: '))
	numeros[0].append(num) if num % 2 == 0 else numeros[1].append(num)
print(f'Os números pares digitados foram: {sorted(numeros[0])}')
print(f'Os números impares digitados foram: {sorted(numeros[1])}')
