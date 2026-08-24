from os import system
boletim = list()
while True:
	nome = str(input('Nome:'))
	nota1 = float(input('Nota 1: '))
	nota2 = float(input('Nota 2: '))
	boletim.append([nome, nota1, nota2])
	resp = input('Deseja continuar? [S/N]')
	system('clear')
	if resp in 'Nn':
		break

print(f'{"N°.":<4}{"Nome":<10}{'Média':>6}')
print('==' * 10)
for i, (name, n1, n2) in enumerate(boletim):
	print(f'{i:<4}{name:<10}{(n1 + n2)/ 2:>6}')

while True:
	print('==' * 20)
	num = int(input('Mostrar notas de qual aluno?(999 interrompe): '))
	print('==' * 20)
	if num == 999:
		break
	print(f'As notas de {boletim[num][0]} são [{boletim[num][1]}],[{boletim[num][2]}]') 

print('Volte sempre')