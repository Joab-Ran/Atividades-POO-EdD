"""Quicksort"""
def __quicksort__(lista):
    num = len(lista)
    for i in range(num):
        minimo = i
        for j in range(i+1,num):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

vals = [100,-7,12,37,2]
print(f"Antes da ordenação {vals}")
__quicksort__(vals)
print(f"Depois da ordenação {vals}")
