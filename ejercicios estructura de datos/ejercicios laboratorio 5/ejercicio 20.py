# ejercicio 20
#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
#palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor.

def palabras_palindromas_longitud_ordenadas(conjunto_palabras, longitud):
   
    #Devuelve un conjunto con las palabras palíndromas de longitud determinada, ordenadas de menor a mayor.


    palindromos_longitud_ordenados = {palabra for palabra in conjunto_palabras if len(palabra) == longitud and palabra == palabra[::-1]}
    palindromos_longitud_ordenados = sorted(palindromos_longitud_ordenados)  # Ordena las palabras palíndromas de menor a mayor
    return set(palindromos_longitud_ordenados)

# Ejemplo 
conjunto_palabras = {"radar", "oso", "casa", "reconocer", "sol", "ana"}
longitud = 3
palindromos_longitud_ordenados = palabras_palindromas_longitud_ordenadas(conjunto_palabras, longitud)
print(f"El conjunto de palabras palíndromas de longitud {longitud} ordenadas de menor a mayor es:", palindromos_longitud_ordenados)
