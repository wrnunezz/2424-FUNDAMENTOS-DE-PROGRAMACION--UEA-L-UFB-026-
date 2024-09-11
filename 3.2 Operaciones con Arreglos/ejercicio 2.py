#ejercicio 2 Matriz de 3 x 3
matriz = [
    [1, 13, 9],
    [2, 11, 4],
    [3, 8, 3]
]

print(matriz)
# metodo de ordenamiento buble_sort
def buble_sort(fila):
    #algoritmo buble sort
    n = len(fila)
    for i in range(n):
        for j in range(n-1, i,-1):
            if fila[j] > fila[j-1]:
                fila[j], fila[j-1] = fila[j-1], fila[j]
                print(fila)

print("Matriz original ")
print(matriz)
buble_sort(matriz[0])
print(matriz)



