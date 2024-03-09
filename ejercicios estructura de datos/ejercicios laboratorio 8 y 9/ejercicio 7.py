#7 Asegurar que una función retorna un valor específico.
def suma(a, b):
    resultado = a + b
    return resultado
assert suma(3, 4) == 7, "La función no retornó el valor esperado"

print("La función retornó el valor esperado")
