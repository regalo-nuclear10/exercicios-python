print('Gerador de PA')
print('==' * 15)
Primeiro = int(input('Primeiro termo: '))
Termo = Primeiro
Razão = int(input('Razão da PA: '))
c = 0
Tot_termos = 0
Outros_termos = 1
while c < 10:
	print(Termo, end= ' > ')
	Termo += Razão
	Tot_termos += 1
	c += 1
print('Acabou')
while Outros_termos != 0:
	Outros_termos = int(input('Quantos termos quer mostrar a mais? '))
	for C in range(0 , Outros_termos):
		Tot_termos += 1
		print(Termo, end=' > ')
		Termo += Razão
	print('Acabou')
print(f'Ao todo foram mostrados {Tot_termos} termos da PA de {Primeiro} com razão {Razão}')
	