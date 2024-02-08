import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_province = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\covid19_region _python.csv",sep=";")
df_comuni = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\comuni_clean (1).csv",sep=";")

# Filter data for small municipalities (population <= 10,000)
comuni_10000_50000 = df_comuni[(df_comuni['Popolazione2011'] > 10000) & (df_comuni['Popolazione2011'] <= 50000)]
merge_per_comuni_10000_50000 = pd.merge(df_province, comuni_10000_50000, how='inner', left_on='RegionName', right_on='Regione')
merge_per_comuni_10000_50000['Incidenza'] = (merge_per_comuni_10000_50000['TotalPositiveCases'] / merge_per_comuni_10000_50000['Popolazione2011']) * 100

incidenza_comuni_10000_50000 = merge_per_comuni_10000_50000[['Denominazione', 'Regione', 'Incidenza']]

comuni_50000 = df_comuni[df_comuni['Popolazione2011'] > 50000]

merge_per_comuni_50000 = pd.merge(df_province, comuni_50000, how='inner', left_on='RegionName', right_on='Regione')

merge_per_comuni_50000['Incidenza'] = (merge_per_comuni_50000['TotalPositiveCases'] / merge_per_comuni_50000['Popolazione2011']) * 100

incidenza_comuni_50000 = merge_per_comuni_50000[['Denominazione', 'Regione', 'Incidenza']]


plt.figure(figsize=(12, 6))
sns.barplot(x=comuni_10000_50000, y=totali_positivi_regione.values)
plt.xticks(rotation=45)
plt.xlabel('Regione')
plt.ylabel('Totale positivi')
plt.title('Totale Positivi per Regione')
plt.show()

'''
plt.figure(figsize=(12, 4))

plt.subplot(131) 
sns.barplot(x='Denominazione', y='Incidenza', data=incidenza_comuni_50000.head(10)) 
plt.xlabel('Comune') 
plt.ylabel('Incidenza') 
plt.title('Incidenza dei casi positivi per comune (<= 10.000 abitanti)') 
plt.xticks(rotation=45)

plt.subplot(132) 
sns.barplot(x='Denominazione', y='Incidenza', data=incidenza_comuni_10000_50000.head(10)) 
plt.xlabel('Comune') 
plt.ylabel('Incidenza') 
plt.title('Incidenza dei casi positivi per comune (10.000 - 50.000 abitanti)') 
plt.xticks(rotation=45)

plt.subplot(133) 
sns.barplot(x='Denominazione', y='Incidenza', data=incidenza_comuni_50000.head(10)) 
plt.xlabel('Comune') 
plt.ylabel('Incidenza') 
plt.title('Incidenza dei casi positivi per comune (> 50.000 abitanti)') 
plt.xticks(rotation=45)

plt.tight_layout() 
plt.show()'''