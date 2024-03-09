#3 Validar el rango de una calificación.
calificacion = float(input("ingrese su calificacion: "))
assert 0<=calificacion <=20, " la calificacion debe estar en el rango de 1 a 20"
print(" la calificacion",calificacion,"es valida")
                
