#ejercicio 7
#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
#anagramas
def encontrar_anagramas(conjunto_palabras):
    
    anagramas = set()
    # Utiliza un diccionario para agrupar las palabras por sus letras ordenadas
    palabras_agrupadas = {}
    for palabra in conjunto_palabras:
        letras_ordenadas = ''.join(sorted(palabra))
        if letras_ordenadas in palabras_agrupadas:
            palabras_agrupadas[letras_ordenadas].add(palabra)
        else:
            palabras_agrupadas[letras_ordenadas] = {palabra}
    
    # Encuentra las palabras que tienen más de un anagrama en el conjunto
    for palabras in palabras_agrupadas.values():
        if len(palabras) > 1:
            anagramas.update(palabras)

    return anagramas

# Ejemplo 
conjunto_palabras = {"amor", "roma", "mar", "rama", "perro", "roper"}
anagramas = encontrar_anagramas(conjunto_palabras)
print("El conjunto de palabras que son anagramas entre sí es:", anagramas)
