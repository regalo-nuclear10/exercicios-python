print('==' * 20)
print(f'{'DETECTOR DE PALÍNDROMO':^40}')
print('==' * 20)
frase = str(input('Digite uma frase: ')).replace(' ','').upper()
palíndromo = frase[::-1]
if frase == palíndromo:
	print('A frase é um palíndromo.')
	print(f'E ao contrário fica {palíndromo}')
else:
	print('A frase não é um palíndromo')
	print(f'O inverso de {frase} é \033[35m{palíndromo}\033[m')