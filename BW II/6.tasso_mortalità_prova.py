import pandas as pd 
import matplotlib.pyplot as plt

df_province = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\covid19_region _python.csv",sep=";") 
df_comuni = pd.read_csv(r"C:\Users\marco\OneDrive\Documenti\GitHub\digichamps2\BW II\comuni_clean (1).csv",sep=";")

merged_df = pd.merge(df_province, df_comuni, left_on="RegionName", right_on="Denominazione")

merged_df["TassoMortalità"] = (merged_df["Deaths"] / merged_df["Popolazione2011"]) * 1000

plt.scatter(merged_df["Popolazione2011"], merged_df["TassoMortalità"]) 
plt.xlabel("Popolazione 2011")
plt.ylabel("Tasso Mortalità per Covid-19 (per 1000 abitanti)")
plt.title("Relazione tra Popolazione 2011 e Tasso Mortalità per Covid-19") 
plt.show()

total_deaths = merged_df["Deaths"].sum() 
total_population = merged_df["Popolazione2011"].sum()

mortality_rate = (total_deaths / total_population) * 1000

print("Numero totale dei morti rapportato alla popolazione: ", mortality_rate)

import matplotlib.pyplot as plt

# Calculate mortality rate
total_deaths = merged_df["Deaths"].sum()
total_population = merged_df["Popolazione2011"].sum()
mortality_rate = (total_deaths / total_population) * 1000

# Create a bar chart
plt.bar("Mortality Rate", mortality_rate)

# Set labels and title
plt.ylabel("Mortality Rate")
plt.title("Mortality Rate per 1000 Population")

# Display the chart
plt.show()