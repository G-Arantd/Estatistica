import pandas as pd

tabela = pd.read_csv("TabelaQuartis.csv")

df = pd.DataFrame(tabela)

print (df["salarios (mt)"])