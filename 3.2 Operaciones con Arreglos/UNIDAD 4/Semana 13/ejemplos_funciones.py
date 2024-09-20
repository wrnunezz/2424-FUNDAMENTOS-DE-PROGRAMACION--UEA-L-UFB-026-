# definir una función para listas

# def mostrar_lista(lista):
#     for elemento in lista:
#         print(elemento)
#
# apellidos = ['Perez','Lopez','Martinez',25,25.5]
#
# mostrar_lista(apellidos)

#() tupla
#[] lista
#{} dicci
def mostrar_elementos(diccionario):
    for clave,valor in diccionario.items():
        print(f'est es mi atributo clave : {clave} y este el valor  :{valor}')


dicc_nombres = {"Juan":150,"Pedro":200}
mostrar_elementos(dicc_nombres)




