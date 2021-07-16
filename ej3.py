dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
df = pd.DataFrame([[key, dict1[key]] for key in dict1.keys()], columns=['Letra', 'Numero'])
print(df)