import pandas as pd

# Carico il dataset da file txt
dataset = pd.read_csv("Ripartizione-geografica _python.txt", delimiter="\t", encoding="latin-1")

# Stampo le prime 5 righe del dataset
print(dataset.head())

# Calcolo il numero totale di regioni presenti nel dataset
numero_regioni = dataset["Regione"].nunique()
print("Numero di regioni:", numero_regioni)

# Conto il numero di ripartizioni per ogni regione
conteggio_ripartizioni = dataset.groupby("Regione")["Ripartizione geografica"].nunique()
print("Conteggio delle ripartizioni per ogni regione:")
print(conteggio_ripartizioni)