
# Tupla
valores = (1258,2000,3553564,665876.19,"HDD Farm Road", 75000.00, "39° 25.25'' 25.216358''")

# con LIST() Convierto TUPLA en LISTA
listaValores = list(valores)

# y en la LISTA SI PUEDO AGREGAR VALORES
listaValores.append("Nuevo Elemento")
print(listaValores)
print(type(listaValores))

nuevaTuplaValores  = tuple(listaValores)
print(nuevaTuplaValores)
print(type(nuevaTuplaValores))



