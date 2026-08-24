l = float(input('Qual a largura da parede em metros: '))
h = float(input('Qual a altura da parede em metros: '))
A = l * h
litro = A / 2
print(f" A sua parede tem uma area de {A:.1f}m^2, com uma altura de {h}m e a largura de {l}m")
print(f"Considerando que cada litro de tinta pinta um area de 2m^2, voce precisa de {litro} de tinta")