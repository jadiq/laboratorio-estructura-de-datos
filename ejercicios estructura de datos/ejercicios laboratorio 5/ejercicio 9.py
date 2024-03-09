#ejercicio 9

#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#tienen una longitud determinada.
def palabras_con_longitud(conjunto_palabras, longitud):
#Encuentra las palabras en el conjunto dado que tienen la longitud especificada.
    palabras_longitud_determinada = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    return palabras_longitud_determinada

# Ejemplo
conjunto_palabras = {"gato", "perro", "oso", "elefante", "ave"}
longitud_deseada = 4
palabras_longitud_determinada = palabras_con_longitud(conjunto_palabras, longitud_deseada)
print(f"El conjunto de palabras de longitud {longitud_deseada} es:", palabras_longitud_determinada)
