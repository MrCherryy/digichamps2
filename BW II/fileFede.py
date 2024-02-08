import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_regioni = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\covid19_region _python.csv",sep=";")
df_air = pd.read_csv("https://github.com/andreapas79/COVID-19/raw/master/df_air.csv", index_col=0)

print(df_air)
df_comuni = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\comuni_clean (1).csv",sep=";")

# sostituisco P.A. di Bolzano e P.A. Trento con Trentino Alto Adige
df_air['Regione'] = df_air.iloc[:,2].replace('P.A. Trento', 'Trentino Alto Adige')
df_air['Regione'] = df_air.iloc[:,2].replace('P.A. Bolzano', 'Trentino Alto Adige')
print(df_air)

tot_deaths = df_regioni.groupby('RegionName')['Deaths'].sum()
df_deaths = tot_deaths.to_frame().reset_index()

tot_popolazione = df_comuni.groupby("Regione")["Popolazione2011"].sum()
df_pop = tot_popolazione.to_frame().reset_index()

df_summary = df_deaths.merge(tot_popolazione, left_on='RegionName', right_on='Regione')

df_air_med = df_air.groupby(['Regione']).agg({'max media annuale (mg/m3)': ['count', 'mean', 'median']})
df_air_med = df_air_med.reset_index()
print(df_air_med)
df_summary['death%'] = (df_summary['Deaths']/df_summary['Popolazione2011'])*100
# print(df_summary)

df_air_med.columns = df_air_med.columns.get_level_values(0)

df_summary = df_summary.sort_values(by='death%', ascending=False).merge(df_air_med, left_on='RegionName',right_on='Regione')




df_summary_sorted = df_summary.sort_values(by='death%', ascending=False).reset_index(drop=True)
# #print(df_summary_sorted)

df_air_med_sorted = df_air_med.sort_values(by=('max media annuale (mg/m3)', 'median'), ascending=False)
# print(df_air_med_sorted)

df_summary = df_summary = df_summary.sort_values(by='death%', ascending=False).merge(df_air_med, left_on='RegionName',right_on='Regione')

#df_summary = df_summary_sorted.merge(df_air_med_sorted, left_on='RegionName',right_on='Regione')
# df_summary = df_summary.iloc[:,[0,1,2,3,7]]
# df_summary.columns = ['codice_regione',
#                'denominazione_regione',
#                             'deceduti',
#                          'popolazione',
#                               'death%',
#                      'air_poll_median']

# heatmapshow = df_summary[['denominazione_regione',
#                                        'deceduti',
#                                          'death%',
#                                     'popolazione',
#                                 'air_poll_median']].corr()

# plt.figure(figsize=(20,10))
# plt.subplot(122)
# sns.scatterplot(x=df_summary.iloc[:,5], y= df_summary['death%'], data=df_summary, hue='air_poll_median', s=500)
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# plt.subplot(121)
# sns.heatmap(heatmapshow, annot=True, annot_kws={'size':20})