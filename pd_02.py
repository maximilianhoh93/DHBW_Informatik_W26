import pandas as pd

# Bitte noch folgende Module installieren
# pip install matplotlib
# pip install openpyxl

df = pd.read_csv('Data_dup.csv') # wir lesen die CSV-Datei in einen DataFrame ein
print(df) # wir geben den DataFrame aus
df_dupResul=df.duplicated() 
# wir schauen nach, ob es Duplikate gibt
i=0
print(df_dupResul)
a=0

for Ergebnis in df_dupResul:
    print(Ergebnis)
    if Ergebnis == True:
        a=a+1
    # zählen sie alle dupilicates
    # Ergebnis ist entweder True oder False
    # je nachdem ob es ein Duplikat ist oder nicht
print("Anzahl der Duplikate:", a)

print(i)

df.drop_duplicates(keep=False, inplace=True)


df.drop_duplicates(keep='first',inplace=True)
# die Duplikate werden entfernt, nur das erste Vorkommen bleibt erhalten




df_dupResul=df.duplicated()
print(df_dupResul)
# wir schauen nach, ob alle Duplikate entfernt wurden 
df.to_excel("Data_dup2.xlsx")


