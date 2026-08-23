print( '--' * 15)
print(f'{"\033[36mEmpréstimo bancário\033[m":^35}')
print('--' * 15)
casa = float(input('Qual o valor da casa? R$ '))
salário = float(input('Qual o seu salário? R$'))
ano = int(input('Em quantos anos vai nos pagar de volta? '))
prestação = casa / (ano * 12)
if prestação > salário * 30 / 100:
	print('\033[31mEmpréstimo NEGADO!\033[m')
	print('Infelizmente você não pode financiar esta casa')
else:
	print(f'\033[32mO seu impréstimo foi aprovado!\033[m\n O Sr. parcelou em {ano} anos um valor de R${casa:.2f} e deverá nos pagar mensalmente R${prestação:.2f}')