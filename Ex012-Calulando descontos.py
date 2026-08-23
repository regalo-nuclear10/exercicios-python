Preço = float(input("Qual é o preço do produto? R$"))
NP = Preço - (Preço * 5 / 100)
print( f'O preço do produto custava R$ {Preço:.2f}\n Na promoção de 5% vai custar R${NP:.2f}')