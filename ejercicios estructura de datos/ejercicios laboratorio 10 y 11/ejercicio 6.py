
# Ejercicios parte 02:
# 6 Utilizar una pila para invertir el orden de los caracteres de una cadena.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items)-1]

def invertir_cadena_con_pila(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()
    return cadena_invertida

cadena_original = "buenas noches!"
cadena_invertida = invertir_cadena_con_pila(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
