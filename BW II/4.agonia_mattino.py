import pandas as pd
import matplotlib.pyplot as plt

df_province = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\covid19_region _python.csv",sep=";")
df_comuni = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\comuni_clean (1).csv",sep=";")

df_comuni_meno_10000 = df_comuni[df_comuni['Popolazione2011'] < 10000]

df_covid_comuni_meno_10000 = df_province[df_province['RegionName'].isin(df_comuni_meno_10000['Regione'])]

df_incidenza = df_covid_comuni_meno_10000.groupby('RegionName')['TotalPositiveCases'].sum() / df_comuni_meno_10000.groupby('Regione')['Popolazione2011'].sum() * 100

df_incidenza.plot(kind='bar', colormap='plasma')
plt.xlabel('Regione')
plt.ylabel('Incidenza (%)')
plt.title('Incidenza del COVID-19 nei comuni con meno di 10000 abitanti per regione')
plt.xticks(rotation=45)
plt.show()

df_comuni_piu_50000 = df_comuni[df_comuni['Popolazione2011'] > 50000]
df_covid_comuni_piu_50000 = df_province[df_province['RegionName'].isin(df_comuni_piu_50000['Regione'])]
df_incidenza_piu_50000 = df_covid_comuni_piu_50000.groupby('RegionName')['TotalPositiveCases'].sum() / df_comuni_piu_50000.groupby('Regione')['Popolazione2011'].sum() * 100
df_incidenza_piu_50000.plot(kind='bar', colormap='plasma')
plt.xlabel('Regione')
plt.ylabel('Incidenza (%)')
plt.title('Incidenza del COVID-19 nei comuni con più di 50000 abitanti per regione')
plt.xticks(rotation=45)
plt.show()

df_comuni_tra_10000_50000 = df_comuni[(df_comuni['Popolazione2011'] >= 10000) & (df_comuni['Popolazione2011'] <= 50000)]
df_covid_comuni_tra_10000_50000 = df_province[df_province['RegionName'].isin(df_comuni_tra_10000_50000['Regione'])]
df_incidenza_tra_10000_50000 = df_covid_comuni_tra_10000_50000.groupby('RegionName')['TotalPositiveCases'].sum() / df_comuni_tra_10000_50000.groupby('Regione')['Popolazione2011'].sum() * 100

df_incidenza_tra_10000_50000.plot(kind='bar', colormap='plasma')
plt.xlabel('Regione')
plt.ylabel('Incidenza (%)')
plt.title('Incidenza del COVID-19 nei comuni con tra 10000 e 50000 abitanti per regione')
plt.xticks(rotation=45)
plt.show()

'''
df_covid_per_regione = df_province.groupby('RegionName')['TotalPositiveCases'].sum()
df_incidenza_per_regione = df_covid_per_regione / df_comuni.groupby('Regione')['Popolazione2011'].sum() * 100

df_incidenza_per_regione.plot(kind='bar', colormap='plasma')
plt.xlabel('Regione')
plt.ylabel('Incidenza (%)')
plt.title('Incidenza del COVID-19 nelle regioni per comuni')
plt.xticks(rotation=45)
plt.show()
'''