import pandas as pd
from apyori import apriori

dados = pd.read_csv('C:/WorkspacePython/data-sets/itens-cupom-44.csv', sep=';', header = None)

transacoes = []
for i in range(0, 10):
    transacoes.append([str(dados.values[i, j]) for j in range(0, 4) ])

regras = apriori(transacoes, min_support=0.1, min_confidence=0.8, min_lift=2, min_lenght=2)
resultados = list(regras)

resultados2 = [list(x) for x in resultados]

resultadoFormatado = []
for j in range(0, 93):
    resultadoFormatado.append([list(x) for x in resultados2[j][2]])
print(resultadoFormatado)