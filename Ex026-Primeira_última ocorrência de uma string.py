frase = str(input(' Digite uma frase: ')).strip()
print(f' A letra "A" aparece na frase {frase.upper().count('A')} vezes')
print(f' A primeira letra "A" apareceu na posição {frase.find('A') + 1}')
print(f' A última letra "A" aparece na posição {frase.rfind('A') + 1}')