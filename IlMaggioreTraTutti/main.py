
lista_numeri = [42, 9, 23, 11, 17, 56, 3]
numero_maggiore = lista_numeri[0]
for numero in lista_numeri:
    if numero > numero_maggiore:
        numero_maggiore = numero
print("Il numero maggiore tra tutti è:", numero_maggiore)