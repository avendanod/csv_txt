miTupla = (1258,2000,3553564,665876.19,"HDD Farm Road", 75000.00, "39° 25.25'' 25.216358''")

miLista = list(miTupla)

miLista.insert(5,"Francia")

nuevaTupla = tuple(miLista)

print(nuevaTupla)

miLista2 = list(nuevaTupla)

miLista2.remove(65000.0)

nuevaTupla2 = tuple(miLista2)

print(nuevaTupla2)




