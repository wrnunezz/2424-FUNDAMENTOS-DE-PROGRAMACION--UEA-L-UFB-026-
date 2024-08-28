# Matriz de 3 x 3
matriz = [
    [8, 13, 9],
    [2, 10, 4],
    [6, 8, 3]
]

print(matriz)

# funcion buscar_valor especifico
def buscar_valor(matriz,valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == valor_buscado:
                return i,j

valor_buscado = 10
#print(buscar_valor(matriz,valor_buscado))

if valor_buscado == valor_buscado:
    print("valor encontrado en la posición",buscar_valor(matriz,valor_buscado))
else:
    print("Valor incorrecto")


