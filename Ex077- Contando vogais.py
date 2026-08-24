palavras = ('Aprender', 'Python', 'Amor', 'Enzo', 'Curso', 'Casaco')
for palavra in palavras:
	print(f'Na palavra {palavra.upper()} temos as vogais:', end=' ')
	for letra in palavra:
		if letra.lower() in 'aeiou':
			print(letra.lower(), end=' ')
	print('\n')