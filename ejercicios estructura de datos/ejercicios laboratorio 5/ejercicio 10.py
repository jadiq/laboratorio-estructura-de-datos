#ejercicio 10
#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que 
#contienen una letra determinada.
def palabras_con_letra(conjunto_palabras, letra):

    palabras_con_la_letra = {palabra for palabra in conjunto_palabras if letra in palabra}
    return palabras_con_la_letra

# Ejemplo
conjunto_palabras = {"gato", "perro", "oso", "elefante", "ave"}
letra_deseada = "o"
palabras_con_la_letra = palabras_con_letra(conjunto_palabras, letra_deseada)
print(f"El conjunto de palabras que contienen la letra '{letra_deseada}' es:", palabras_con_la_letra)

