#Ejercicio parte 01:

#1 Validar la edad de un usuario.
edad = int(input("ingrese su edad: "))
assert 1 <= edad <= 110, "La edad no es valida"
print(edad, "es valido")

