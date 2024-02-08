# Andamento per mese dei nuovi casi positivi senza dividerlo per regione. Com'è andato in Italia il covid, e.g trovare il picco 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np 

df_regione = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\covid19_region _python.csv",sep=";") 

df_regione['Date'] = pd.to_datetime(df_regione['Date'], dayfirst=True)

df_regione['Month'] = df_regione['Date'].dt.month

andamento_casi_anno = df_regione.groupby('Month')['NewPositiveCases'].sum() 

plt.figure(figsize=(12, 6))
sns.barplot(x=andamento_casi_anno.index, y=andamento_casi_anno.values)
plt.xlabel('Mese')
plt.ylabel('Nuovi casi positivi')
plt.title('Andamento Mensile dei Nuovi Casi Positivi in Italia')
plt.show()