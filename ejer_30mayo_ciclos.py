# Métodos para tuplas () - inmutables(no se pueden editar)

nombres = ("ÓSCAR", "INGRID", "ALEXANDER", "KAREN", "CAMILO", "LUIS", "KEVIN", "INGRID")

""" # Método len(): devuelve la longitud de la tupla, # de elementos de la tupla

print(len(nombres))

# Método count(): cuenta el número de veces que aparece un elemento específico en la tupla

print(nombres.count("INGRID"))
print(nombres.count("ALEXANDER"))

# Método index(): devuelve el índice o posición de la primera aparición de un elemento en la tupla

print(nombres.index("CAMILO"))
# print(nombres.index("INÉS")) #genera error porque no existe en la tupla
 """
print(nombres)

# Método list(): Convertir una tupla a una lista

lista_nombres = list(nombres)
print(lista_nombres)

# Ejemplo de Try ... except

nombres = ("ÓSCAR", "INGRID", "ALEXANDER", "KAREN", "CAMILO", "LUIS", "KEVIN", "INGRID")

try:
    print(nombres.index("INES"))
except ValueError:
    print("El nombre no existe en la tupla")

lista_nombres = list(nombres)
print(lista_nombres)
print(nombres.count("INGRID"))
print(nombres.count("ALEXANDER"))