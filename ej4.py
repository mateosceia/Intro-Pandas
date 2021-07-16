dict1 = {"a": [1,3,5,2], "b": [4,2,3,5]}
dict2 = {}
for clave,valor in dict1.items():
    pares = []
    impares = []
    potencia = []
    for i in range(0,len(valor), 2):
        pares.append(valor[i])
    for i in range(1, len(valor), 2):
        impares.append(valor[i])
    for i in range(len(pares)):
        potencia.append(pares[i]** impares[i])
    dict2[clave] = potencia

print(dict2)

new_df = pd.DataFrame(dict2)
print(new_df)            