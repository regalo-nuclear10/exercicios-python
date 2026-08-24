Média = 0
Maior_idade = 0
Menor_20 = 0
for people in range(1, 5):
	print(f'{people}° Pessoa:')
	nome = str(input('Nome: ')).strip()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo[M/F]: ')).upper()
	Média += idade
	if sexo == 'M':
		if people == 1:
			Maior_idade = idade
			H_mais_velho = nome
		if idade > Maior_idade:
			Maior_idade = idade
			H_mais_velho = nome
	if sexo == 'F':
		if idade < 20:
			Menor_20 += 1
print(f'O nome do homem mais velho é {H_mais_velho} com uma idade de {Maior_idade} anos\n')
print(f'O número de mulheres q tem menos de 20 anos é {Menor_20}')
print(f'E a média de idade do grupo é {Média / 4:.0f} anos')
