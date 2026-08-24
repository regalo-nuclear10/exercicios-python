print('=' * 46)
print(f'{"Passagem de Autocarros":^46}')
print('=' * 46)
d = float(input(f' Qual é a distância até o seu destino?(Km):'))
if d <= 200:
	passagem = d * 0.50
else:
	passagem = d * 0.45
print(f' A sua viagem é de {d} Km, e a passagem vai custar R${passagem:.2f}')