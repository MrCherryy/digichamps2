import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df_province = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\covid19_region _python.csv",sep=";") 
df_comuni = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\comuni_clean (1).csv",sep=";")

tot_decessi = df_province.groupby("RegionName")["Deaths"].sum().sum()
tot_popolazione = df_comuni.groupby("Regione")["Popolazione2011"].sum().sum()
rapporto = tot_decessi / tot_popolazione
print(rapporto)

sns.set_palette("pastel")
etichette = ["Decessi 2020", "Popolazione 2011"]
sizes = [tot_decessi, tot_popolazione]
plt.pie(sizes, labels=etichette, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title("Rapporto tra decessi e popolazione")
plt.show()