# ejercicio 17
#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#tienen una longitud determinada y están ordenadas de menor a mayor.

def palabras_por_longitud(conjunto, longitud):
    palabras_filtradas = set()

    for palabra in conjunto:
        if len(palabra) == longitud:
            palabras_filtradas.add(palabra)

    palabras_ordenadas = sorted(palabras_filtradas)
    return set(palabras_ordenadas)

mi_conjunto = {"lunes", "martes", "miercoles", "jueves", "viernes"}
longitud1 = 6
palabras_filtradas2 = palabras_por_longitud(mi_conjunto, longitud1)
print(palabras_filtradas2)
