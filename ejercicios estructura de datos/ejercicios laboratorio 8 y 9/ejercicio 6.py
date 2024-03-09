#6 Asegurar que un ciclo while se ejecuta al menos una vez.
contador = 0
while contador < 5:
    contador +=1
assert contador == 5, "el ciclo white no se ejecuto"
print("el ciclo while se ejecuto", contador,"veces")


