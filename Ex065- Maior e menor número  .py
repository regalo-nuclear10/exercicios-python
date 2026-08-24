resp = 'S'
Cont = Soma = 0
while resp == 'S':
	núm = int(input('Digite um número inteiro: '))
	Soma += núm
	Cont += 1
	if Cont ==1:
		Maior = Menor = núm
	else:
		if núm > Maior:
			Maior = núm
		if núm < Menor:
			Menor = núm
	resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
Média = Soma / Cont
print(f'Entre os {Cont} valores digitados o maior foi {Maior} e o menor foi {Menor}.\nE a média entres os números é {Média}')
