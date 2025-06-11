import pandas as pd

data = {
    'ID': [1, 2, 3],
    'Nombre': ['Ana', 'Carlos', 'Lucía'],
    'Edad': [34, 28, 45],
    'Sexo': ['F', 'M', 'F'],
    'Peso': [62, 75, 70],
    'Altura': [1.65, 1.80, 1.70]
}

df = pd.DataFrame(data)
df.to_csv('pacientes.csv', index=False)