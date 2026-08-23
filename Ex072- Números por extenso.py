from time import sleep
Extenso = ('zero', ' um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')
while True:
	núm = int(input('Digite um número entre 0 e 20: '))
	while not 0 <= núm <= 20:
		núm = int(input('Tente novamente. Digite um número entre 0 e 20: '))
	print(f'O número {núm} por extenso escreve-se {Extenso[núm]}')
	sleep(1)
	while True:
		resp = str(input('Deseja continuar?[S/N]: ')).upper().strip()[0]
		if resp in 'SN':
			break
	print('==' * 15) 
	if resp == 'N':
		break
print('Programa finalizado!')
	