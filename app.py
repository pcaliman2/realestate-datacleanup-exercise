import pandas as pd

data = pd.DataFrame({
    'id': [1, 2, 3],
    'nombre': ['Ana', 'Luis', 'Carlos'],
    'edad': [25, 30, 35]
}).set_index('id')

df = pd.DataFrame(data)
df.to_csv('pacientes.csv', index=False)