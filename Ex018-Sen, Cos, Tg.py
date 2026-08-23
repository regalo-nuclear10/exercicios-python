import math
Ângulo = float(input(" Digite o ângulo q deseja: "))
Seno = math.sin(math.radians(Ângulo))
Cos = math.cos(math.radians(Ângulo))
Tg = math.tan(math.radians(Ângulo))
print(f" O ângulo de {Ângulo} tem como SENO: {Seno:.2f}\n O ângulo de {Ângulo} tem como COSSENO: {Cos:.2f}\n O ângulo de {Ângulo} tem como TANGENTE: {Tg:.2f}")