Km = float(input(' Quantos Quilômetros o carro andou? '))
Dia = int(input(' Quantos dias o carro esteve alugado? '))
P = 60 * Dia + 0.15 * Km
print('=' * 30)
print('Conta de aluguel do carro: ')
print('=' * 30)
print(f' Total de dias alugados:{Dia} x R$60\n Total de Km andado:{Km}x R$0.15\n')
print(f' Total a pagar:R${P:.2f }')
