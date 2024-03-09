# 9 Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una
# pila.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

def verificar_anidacion(expresion):
    pila = Pila()
    abrir_parentesis = set(['(', '[', '{'])
    cerrar_parentesis = set([')', ']', '}'])
    parejas_parentesis = {'(': ')', '[': ']', '{': '}'}

    for caracter in expresion:
        if caracter in abrir_parentesis:
            pila.apilar(caracter)
        elif caracter in cerrar_parentesis:
            if pila.esta_vacia():
                return False
            else:
                ultimo_parentesis_abierto = pila.desapilar()
                if parejas_parentesis[ultimo_parentesis_abierto] != caracter:
                    return False

    return pila.esta_vacia()

# Ejemplo de uso
expresion = "((3+2)*5)"
resultado_verificacion = verificar_anidacion(expresion)
if resultado_verificacion:
    print("Los operadores en la expresión están correctamente anidados.")
else:
    print("Los operadores en la expresión no están correctamente anidados.")
