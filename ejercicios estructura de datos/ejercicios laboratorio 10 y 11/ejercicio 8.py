# 8 Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

def evaluar_expresion_posfija(expresion):
    pila = Pila()
    operadores = set(['+', '-', '*', '/'])

    for caracter in expresion:
        if caracter not in operadores:
            pila.apilar(int(caracter))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if caracter == '+':
                resultado = operando1 + operando2
            elif caracter == '-':
                resultado = operando1 - operando2
            elif caracter == '*':
                resultado = operando1 * operando2
            elif caracter == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)

    return pila.desapilar()

# Ejemplo de uso
expresion_posfija = "34+2*"
resultado_evaluacion = evaluar_expresion_posfija(expresion_posfija)
print(f"El resultado de la expresión posfija '{expresion_posfija}' es: {resultado_evaluacion}")

