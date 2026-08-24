m = float(input(' Digite o valor em metros: '))
cores = {'limpa' : '\033[m', 'preto' : '\033[7;40m', 'roxo' : '\033[35m', 'vermelho' : '\033[31m', 'amarelo' : '\033[33m', 'verde' : '\033[32m'}
fundos = {'roxo' : '\033[1;45m', 'azul' : '\033[1;44m', 'vermelho' : '\033[1;41m', 'amarelo' : '\033[1;43m', 'verde' : '\033[1;42m'}
cm = m * 100
mm = m * 1000
Km = m / 1000
Hm = m / 100
Dam = m / 10
dm = m * 10
print(f' A medida de {m} metros equivale a:\n{cores['preto']} {dm} {cores['limpa']} decimetros\t{cores['vermelho']} {Km} {cores['limpa']} {fundos['vermelho']} Kilometros {cores['limpa']}\n{cm} {cores['limpa']} {fundos['azul']} centrímetros {cores['limpa']}\t{cores['roxo']} {Hm} {cores['limpa']} {fundos['roxo']} Hectometros {cores['limpa']}\n{cores['verde']} {mm} {cores['limpa']} {fundos['verde']} milímetros {cores['limpa']}\t{cores['amarelo']} {Dam}{cores['limpa']} {fundos['amarelo']} Decametros {cores['limpa']}')
