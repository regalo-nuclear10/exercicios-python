Homem = Maior_18 = Mulher_menor20 = Tot = 0
while True:
	idade = int(input('Qual sua idade? '))
	sexo = ' '
	while sexo not in 'MF':
		sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
	if sexo == 'M':
		Homem += 1
		Tot += 1
	if sexo == 'F':
		Tot += 1
		if idade <= 20:
			Mulher_menor20 += 1
	if idade >= 18:
		Maior_18 += 1
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Deseja continuar? [S/N]: ')).strip().			upper()[0]
	if resp == 'N':
		break
print(f'Ao todo foram cadastradas {Tot} pessoas,{Homem} delas são homens.\nEntre eles {Maior_18} são maiores de 18.\n E são {Mulher_menor20} mulheres menor de 20 anos') 
