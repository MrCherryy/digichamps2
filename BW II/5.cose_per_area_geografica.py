import pandas as pd
import matplotlib.pyplot as plt 

# Caricare i dataset
df_province = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\covid19_region _python.csv",sep=";") 
df_comuni = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\comuni_clean (1).csv",sep=";")
df_ripartizioni = pd.read_csv("Ripartizione-geografica _python.txt", delimiter="\t", encoding="latin-1")

df_merged = pd.merge(df_province, df_comuni, left_on=['RegionName'], right_on=['Regione'])
df_merged = pd.merge(df_merged, df_ripartizioni, left_on='RegionName', right_on='Regione')

df_current_positives = df_merged.groupby('Ripartizione geografica')['TotalPositiveCases'].sum()
df_deaths = df_merged.groupby('Ripartizione geografica').apply(lambda x: sum(x['TotalPositiveCases']) / sum(x['Popolazione2011'])*100)
df_recovery_rate = (1 - df_merged.groupby('Ripartizione geografica')['TotalPositiveCases'].sum() / df_merged.groupby('Ripartizione geografica')['Popolazione2011'].sum()) * 100

fig, ax = plt.subplots()

df_current_positives.plot(kind='bar', ax=ax, color='blue', alpha=0.7) 
ax.set_xlabel("Ripartizione geografica") 
ax.set_ylabel("Totale dei current positivi")

plt.show()

df_current_positives.plot(kind='bar')
plt.xlabel('Ripartizione geografica')
plt.ylabel('Positività totali')
plt.title('Positività totali per ripartizione geografica')
plt.show()

df_deaths.plot(kind='bar')
plt.xlabel('Ripartizione geografica')
plt.ylabel('Tasso di mortalità (%)')
plt.title('Tasso di mortalità per ripartizione geografica')
plt.show()

df_recovery_rate.plot(kind='bar')
plt.xlabel('Ripartizione geografica')
plt.ylabel('Tasso di guarigione (%)')
plt.title('Tasso di guarigione per ripartizione geografica')
plt.show()