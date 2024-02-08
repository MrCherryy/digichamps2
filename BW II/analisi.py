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

# Andamento per mese dei nuovi casi positivi senza dividerlo per regione. Com'è andato in Italia il covid, e.g trovare il picco 

df_regione['Date'] = pd.to_datetime(df_regione['Date'], dayfirst=True)

df_regione['Month'] = df_regione['Date'].dt.month

andamento_casi_anno = df_regione.groupby('Month')['NewPositiveCases'].sum() 

plt.figure(figsize=(12, 6))
sns.barplot(x=andamento_casi_anno.index, y=andamento_casi_anno.values)
plt.xlabel('Mese')
plt.ylabel('Nuovi casi positivi')
plt.title('Andamento Mensile dei Nuovi Casi Positivi in Italia')
plt.show()

'''
plt.figure(figsize=(12, 6))
sns.distplot(df_regione['NewPositiveCases'].astype(int))
plt.xlabel('Mese')
plt.ylabel('Nuovi casi positivi')
plt.title('Andamento Mensile dei Nuovi Casi Positivi in Italia')
plt.show()
'''

import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
'''
df_regione["Date"] = pd.to_datetime (df_regione["Date"], dayfirst= True)
df_regione.set_index("Date", inplace=True)
plt.figure(figsize=(12,6))

df_regione.resample("M")["NewPositiveCases"].sum().plot(kind= "line")
df_regione.resample("M")["Deaths"].sum().plot(kind = "line")
plt.legend(["Nuovi Casi positivi", "Decessi"], loc = "best")
plt.title ("Distruzione Temporale dei Decessi")
plt.savefig("Andamento Temporale dei casi positivi vs decessi.png", dpi=200)
plt.show()
'''


# prova
'''
df_regione["Date"] = pd.to_datetime(df_regione["Date"], dayfirst=True)
df_regione.set_index("Date", inplace=True)

totali_positivi_regione = df_regione.groupby(['RegionName'])['CurrentPositiveCases'].sum()
totali_decessi_regione = df_regione.groupby(['RegionName'])['Recovered'].sum()
proporzioni_positivi_regione = totali_positivi_regione / totali_positivi_regione.sum()
proporzioni_decessi_regione = totali_decessi_regione / totali_decessi_regione.sum()
regions = df_regione['RegionName'].unique()
pos = np.arange(len(regions))
fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.barh(pos, proporzioni_positivi_regione, color='blue', label='Nuovi Positivi')
rects2 = ax.barh(pos, proporzioni_decessi_regione, color='red', label='Recovered')
ax.set_yticks(pos)
ax.set_yticklabels(regions)
ax.invert_yaxis()
ax.set_xlabel('Proporzione')
ax.set_title('Distribuzione dei Nuovi Positivi e dei Decessi per Regione')
ax.legend()
plt.show()
'''

# Grafico richiesto da captain Fede


totali_ospedalizzati_regione = df_regione.groupby(['RegionName'])['TotalHospitalizedPatients'].sum() 
totali_terapia_intensiva_regione = df_regione.groupby(['RegionName'])['IntensiveCarePatients'].sum() 
proporzioni_ospedalizzati_regione = totali_ospedalizzati_regione / totali_ospedalizzati_regione.sum()
proporzioni_terapia_intensiva_regione = totali_terapia_intensiva_regione / totali_ospedalizzati_regione.sum()

pos = np.arange(len(totali_ospedalizzati_regione)) 
regions = totali_ospedalizzati_regione.index

fig, ax = plt.subplots(figsize=(12, 6)) 
Ospedalizzati = ax.barh(pos, proporzioni_ospedalizzati_regione, color='blue', label='Ospedalizzati') 
Pazienti_Terapia_Intensiva = ax.barh(pos, proporzioni_terapia_intensiva_regione, color='red', label='Terapia Intensiva') 
ax.set_yticks(pos) 
ax.set_yticklabels(regions) 
ax.invert_yaxis() 
ax.set_xlabel('Proporzione') 
ax.set_title('Distribuzione degli Ospedalizzati totali e in Terapia Intensiva per Regione') 
ax.legend() 
plt.show()