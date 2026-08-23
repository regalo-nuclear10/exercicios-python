from time import sleep
continuar = True
num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
print('Analisando....')
sleep(0.5)

while continuar:
	print('=='* 19)
	print('''[1] Soma
[2] Multiplicação
[3] Comparação
[4] Novos números
[5] Sair do programa''')
	print('==' * 10)
	opção = str(input('Opção: '))
	match opção:
		case '1':
			Soma = num1 + num2
			print(f'A soma de {num1} e {num2} é {Soma}')
			resposta = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
			if resposta == 'N':
				continuar = False
				
		case '2':
			produto = num1 * num2
			print(f'A multiplicação de {num1} por {num2} é igual a {produto}')
			resposta = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]
			if resposta == 'N':
				continuar = False
				
		case '3':
			if num1 > num2:
				print(f'Entre {num1} e {num2}  o maior é {num1}')
			elif num1 == num2:
				print(f'Não existe valor maior, os dois valores são iguais')
			else:
				print(f'Entre {num1} e {num2} o maior é {num2}')
			resposta = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
			if resposta == 'N':
					coninuar = False
		case '4':
			num1 = int(input('Insira o novo valor: '))
			num2 = int(input('Insira o novo valor:  '))
			
		case '5':
			print('Fechando...')
			sleep(1)
			continuar = False
			
		case _:
			print('Opção inválida.Tente outra vez!')