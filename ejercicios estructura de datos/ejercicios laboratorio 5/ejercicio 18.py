# ejercicio 18
#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#contienen una letra determinada y están ordenadas de mayor a menor
def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    
    #Devuelve un conjunto con las palabras que contienen una letra determinada, ordenadas de mayor a menor.

    palabras_con_letra = {palabra for palabra in conjunto_palabras if letra in palabra}
    palabras_con_letra_ordenadas = sorted(palabras_con_letra, reverse=True)  # Ordena las palabras de mayor a menor
    return set(palabras_con_letra_ordenadas)

# Ejemplo
conjunto_palabras = {"casa", "perro", "gato", "caballo", "gallina", "elefante"}
letra = "a"
palabras_con_letra_ordenadas = palabras_con_letra_ordenadas(conjunto_palabras, letra)
print(f"El conjunto de palabras que contienen la letra '{letra}' ordenadas de mayor a menor es:", palabras_con_letra_ordenadas)

