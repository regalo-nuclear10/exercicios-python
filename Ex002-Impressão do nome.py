nome = input('Digite seu nome: ').strip().title()
limpa = '\033[m'
if nome[len(nome) - 1] == 'a' or nome[len(nome) - 1] == 'n':
	print(f'Prazer em te conhecer \033[4;45m{nome}{limpa}!')
else:
	print(f'Prazer em te conhecer \033[1;31m{nome}{limpa}!')