velocidade = float(input('Qual a velocidade do carro: '))
if velocidade > 80:
	multa = (velocidade - 80) * 7
	print(' Multado! você excedeu o limite de velocidade; que é 80Km/h')
	print(f' A sua multa é de R${multa:.2f}')
print(' Tenha um bom dia! Dirija com segurança')