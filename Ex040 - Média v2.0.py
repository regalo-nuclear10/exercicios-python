N1 = float(input('Primeira nota: '))
N2 = float(input('Segunta nota: '))
M = (N1 + N2) / 2
print(f'Com {N1} e {N2}, o aluno tem uma média de {M}')

if M < 5:
	print(' O aluno está \033[31mREPROVADO!\033[m')
	
elif 7 > M >= 5:
	print(' O aluno está em \033[33mRECUPERAÇÃO!\033[m')
	
elif M >= 7:
	print(' O aluno está \033[32mAPROVADO!\033[m')