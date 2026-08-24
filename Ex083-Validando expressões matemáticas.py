lista = list()
expressao = str(input('Digite a expressão: '))
for seccao in expressao:
	if seccao == '(':
		lista.append(seccao)
	elif seccao == ')':
		if lista == []:
			lista.append(seccao)
			break
		else:
			lista.pop()
if not(lista == []):
	print('Expressão errada')
else:
	print('Expressão correcta')
