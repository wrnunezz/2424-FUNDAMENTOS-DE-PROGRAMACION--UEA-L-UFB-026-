"""
Crea una función llamada calcular_descuento que tome dos parámetros:
el monto total de la compra y un valor predeterminado para el porcentaje de descuento
(por ejemplo, 10% por defecto).
La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.

La función debe devolver el monto del descuento calculado.

Llamada a la Función:

Llama a la función calcular_descuento al menos dos veces desde el programa principal.
En una llamada, proporciona el monto total de la compra y
, en la otra, proporciona tanto el monto total de la compra como el porcentaje de descuento.
"""
# crear función para el calculo de descuento
def calcular_descuento(monto_total,porcentaje=10):

    descuento = monto_total * porcentaje/100
    return descuento

monto_total = 2000
descuento = calcular_descuento(monto_total)
print(f"Monto total de {monto_total}: ")
print(f"descuento : {descuento}")

print("*****************************************")
monto_total2 = 2000
descuento = 30
descuento2 = calcular_descuento(monto_total2,descuento)
print(f"Monto total de {monto_total2}: ")
print(f"descuento : {descuento2}")

