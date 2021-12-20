import pandas as pd

d0 = {"Data": [15, 4, 3, 8, 15, 22, 7, 9, 2, 3, 3, 12, 6]}
df = pd.DataFrame(d0)

y = df['Data'].mean()
s = df['Data'].median()
q = df['Data'].mode()
a = df['Data'].quantile(.1)
b = df['Data'].max() - df['Data'].min()
vari = df['Data'].var()
dev = df['Data'].std()

d = {'Info': ["Mean", "Median", "Mode", "Quantile", "Range", "Variance", "StDev"], 'Values': [y, s, q, a, b, vari, dev]}
dx = pd.DataFrame(data=d)
