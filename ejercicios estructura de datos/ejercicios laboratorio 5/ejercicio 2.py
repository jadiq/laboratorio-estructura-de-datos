#ejercicio 2
#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#comienzan con una letra determinada.
def palabras_que_comienzan_con(letra, conjunto_palabras):
    
#Encuentra las palabras en un conjunto que comienzan con una letra determinada.

    palabras_con_letra = {palabra for palabra in conjunto_palabras if palabra.startswith(letra)}
    return palabras_con_letra

# Ejemplo 
conjunto_palabras_ejemplo = {"python", "java", "csharp", "html", "css"}
letra_ejemplo = "c"
palabras_con_letra_c = palabras_que_comienzan_con(letra_ejemplo, conjunto_palabras_ejemplo)
print("El conjunto de palabras que comienzan con la letra 'c' es:", palabras_con_letra_c)
