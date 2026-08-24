n1 = int(input('Digite um número: '))
n2 = int(input(' Digite outro número: '))
n3 = int(input('Digite o último número: '))
Maior = n1
Menor = n1
if n2 < n1 and n2 < n3:
	Menor = n2
	
if n3 < n1 and n3 < n2:
	Menor = n3
	
if n2 > n1 and n2 > n3:
	Maior = n2
	
if n3 > n1 and n3 > n2:
	Maior = n3
print(f' Entre {n1}, {n2} e {n3} \n O maior número digitado foi {Maior}\n E o menor número digitado foi {Menor}')
