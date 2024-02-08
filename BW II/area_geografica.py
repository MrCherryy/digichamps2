import pandas as pd 
import matplotlib.pyplot as plt

df_province = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\covid19_region _python.csv", sep=";") 
df_comuni = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\comuni_clean (1).csv", sep=";")
df_ripartizioni = pd.read_csv("Ripartizione-geografica _python.txt", delimiter="\t", encoding="latin-1")

df_merged = pd.merge(df_province, df_comuni, left_on=['RegionName'], right_on=['Regione']) 
df_merged = pd.merge(df_merged, df_ripartizioni, left_on='RegionName', right_on='Regione')

df_current_positives = df_merged.groupby(['Ripartizione geografica', 'Date'])['TotalPositiveCases'].sum() 
df_deaths = df_merged.groupby(['Ripartizione geografica', 'Date']).apply(lambda x: sum(x['TotalPositiveCases']) / sum(x['Popolazione2011'])*100) 
df_recovery_rate = (1 - df_merged.groupby(['Ripartizione geografica', 'Date'])['TotalPositiveCases'].sum() / df_merged.groupby('Ripartizione geografica')['Popolazione2011'].sum()) * 100

fig, ax = plt.subplots()

df_current_positives['Lombardia'].plot(ax=ax, color='blue', alpha=0.7, label='Lombardia') 
df_current_positives['Puglia'].plot(ax=ax, color='green', alpha=0.7, label='Puglia') 
ax.set_xlabel("Data") 
ax.set_ylabel("Totale dei current positivi")

plt.legend() 
plt.show()

df_deaths['Lombardia'].plot() 
df_deaths['Puglia'].plot() 
plt.xlabel('Data') 
plt.ylabel('Tasso di mortalità (%)') 
plt.title('Tasso di mortalità per ripartizione geografica') 
plt.legend(['Lombardia', 'Puglia']) 
plt.show()

df_recovery_rate['Lombardia'].plot()
df_recovery_rate['Puglia'].plot() 
plt.xlabel('Data') 
plt.ylabel('Tasso di guarigione (%)')
plt.title('Tasso di guarigione per ripartizione geografica')
plt.legend(['Lombardia', 'Puglia']) 
plt.show()