from time import sleep
while True:
	tabuada = int(input('Quer ver a tabuada de qual valor? '))
	print('Processando...')
	sleep(0.5)
	print('=' * 15)
	if tabuada >= 0:
		for C in range(1, 11):
			produto = tabuada * C
			print(f'{tabuada} x {C:02} = {produto}')
		print('=' * 15)
	else:
		break
print('Tabuadas finalizadas')