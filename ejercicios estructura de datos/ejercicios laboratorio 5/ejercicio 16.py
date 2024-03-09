# ejercicio 16
#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
#palíndromos y están ordenadas de menor a mayor

def palabras_palindromas_ordenadas(conjunto_palabras):
   
    #Devuelve un conjunto con las palabras palíndromas ordenadas de menor a mayor
    palindromos_ordenados = {palabra for palabra in conjunto_palabras if palabra == palabra[::-1]}
    palindromos_ordenados = sorted(palindromos_ordenados)  # Ordena las palabras palíndromas de menor a mayor
    return set(palindromos_ordenados)

# Ejemplo 
conjunto_palabras = {"radar", "oso", "casa", "reconocer", "sol", "ana"}
palindromos_ordenados = palabras_palindromas_ordenadas(conjunto_palabras)
print("El conjunto de palabras palíndromas ordenadas de menor a mayor es:", palindromos_ordenados)
