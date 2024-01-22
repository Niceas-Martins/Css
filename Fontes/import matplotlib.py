import matplotlib.pyplot as plt
import pandas as pd

# Seus dados (substitua com os dados reais)
data = {
    'HU': ['HU1', 'HU2', 'HU3', 'HU4', 'HU5', 'HU6', 'HU7', 'HU8', 'HU9', 'HU10'],
    'REFINAMENTO': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'DESENVOLVIMENTO': [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    'CODIFICAÇÃO': [5, 5, 5, 5, 5, 5, 5, 5, 0, 0],
    'AGUARDANDO TESTES': [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    'EM TESTES': [6, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    'EM APROVAÇÃO': [1, 2, 1, 1, 2, 3, 0, 0, 0, 0],
    'FINALIZADO': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# Criar o gráfico de linha
plt.figure(figsize=(12, 6))
for index, row in df.iterrows():
    plt.plot(row.index[1:], row.values[1:], marker='o', label=row['HU'])

# Adicionar rótulos e legenda
plt.title('Lead Time por Etapa - Histórias de Usuário')
plt.xlabel('Fase do Processo')
plt.ylabel('Dias')
plt.legend()

# Mostrar o gráfico
plt.show()