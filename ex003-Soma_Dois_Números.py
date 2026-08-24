n1 = int(input('Digite um número: '))
n2 = int( input('Digite outro número: '))
S = n1+n2
limpa = '\033[m'
print(f' A soma entre \033[36m{n1}{limpa} e \033[31m{n2}{limpa} é \033[35m{S}{limpa}')