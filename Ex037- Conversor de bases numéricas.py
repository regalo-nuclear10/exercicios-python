num = int(input('Digite um número: '))
print('''Escolha uma base para conversão:
	[ 1 ] Para binário
	[ 2 ] Para octal
	[ 3 ] Para hexadecimal''')
print('==' * 20)

opcão =int(input('sua opção: '))
if opcão == 1:
	print(f' O número {num} em binário é {bin(num)[2:]}')
	
elif opcão == 2:
	print(f' O número {num} em octal é {oct(num)[2:]}')
	
elif opcão == 3:
	print(f' O número {num} em hexadecimal é {hex(num)[2:].upper()}')

else:
	print(' Opção inválida. Tente novamente!')