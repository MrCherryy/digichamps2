import pandas as pd

# Carica il file CSV in un DataFrame
df_province = pd.read_csv('covid19_italy_province _python.csv')

# Rimuovi le righe duplicate
df_province = df_province.drop_duplicates()

# Rimuovi le righe con valori mancanti
df_province = df_province.dropna(subset=None)

# Rimuovi spazi vuoti dai valori
df_province = df_province.applymap(lambda x: x.strip() if isinstance(x, str) else x)

print(df_province)