import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

df_regione = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\covid19_region _python.csv",sep=";") 

df_regione.describe()
print(df_regione)

totali_positivi_regione = df_regione.groupby('RegionName')['NewPositiveCases'].sum()

plt.figure(figsize=(12, 6))
sns.barplot(x=totali_positivi_regione.index, y=totali_positivi_regione.values)
plt.xticks(rotation=45)
plt.xlabel('Regione')
plt.ylabel('Totale positivi')
plt.title('Totale Positivi per Regione')
plt.show()