
# Funzione per trovare il massimo tra tre numeri
def maxTra3Numeri(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Chiedi gli input
n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))
n3 = int(input("Inserisci il terzo numero: "))

# CHIAMA la funzione e STAMPA il risultato
risultato = maxTra3Numeri(n1, n2, n3)
print(f"Il numero massimo è: {risultato}")