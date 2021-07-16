#Ejercicio 7
import pandas as pd
datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df = pd.DataFrame(datos_ejemplo, index=labels)
print(df[0:3])

#Ejercicio 8

lista = list(datos_ejemplo.items())

for clave,valor in lista[0:2]:
    print(clave,valor)

#Ejercicio 9

lista[0]
for clave,valor in lista[0]:
    valor = valor.upper()
    print(clave,valor)