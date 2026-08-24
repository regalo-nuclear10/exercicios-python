import math
CO = float(input(" Comprimento do Cateto oposto:"))
CA = float(input(" Comprimento do Cateto adjacente: "))
#H = sqrt((CO ** 2) + (CA ** 2))
#H = (CO ** 2 + CA ** 2 )**(1/2)
H = math.hypot(CO , CA)
print(f"A hipotenusa vai medir {H:.2f}")