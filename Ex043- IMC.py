peso = float(input('Seu peso(Kg): '))
altura = float(input('Sua altura(m): '))
IMC = peso / altura ** 2
print(f'O seu índice de massa corporal é: {IMC:.1f}')

if IMC < 18.5:
	print(' Vc está \033[33mabaixo do peso!\033[m')
elif IMC < 25:
	print('Vc está no seu \033[32mpeso ideal!\033[m')
elif IMC < 30:
	print('Vc está com \033[31msobrepeso!\033[m')
elif IMC < 40:
	print('Vc está com obesidade!')
elif IMC > 40:
	print(f'Vc tem \033[7;40mobesidade mórbida\033[m')
