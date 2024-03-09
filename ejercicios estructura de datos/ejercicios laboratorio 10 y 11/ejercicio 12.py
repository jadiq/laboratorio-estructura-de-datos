# 12 Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar
# expresiones.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

def calcular_expresion(expresion):
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

# Ejemplo 
expresion_a_calcular = "32+5*"
resultado_calculo = calcular_expresion(expresion_a_calcular)
print(f"El resultado de la expresión '{expresion_a_calcular}' es: {resultado_calculo}")
