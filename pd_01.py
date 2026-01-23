# Bitte noch folgende Module installieren
# pip install pandas
# pip install matplotlib
# pip install openpyxl
import pandas as pd

df = pd.read_csv('Data_dup.csv') # wir lesen die CSV-Datei in einen DataFrame ein
#df = pd.read_excel('Data_dup3.xlsx')

print(df)









df.dropna(inplace = True) # wir entfernen alle Zeilen mit fehlenden Werten (NaN)

print(df) # wir geben den DataFrame aus


""" # for index,row in df.iterrows(): # wir gehen jede Zeile durch
#     print(row) # die ganze Zeile wird ausgegeben
#     print(index,row.Duration, row.Calories) # wir geben den Index und die Werte in den Spalten 'Duration' und 'Calories' aus
#     print() # eine Leerzeile zur besseren Lesbarkeit
#     if index == 5: # wir suchen die Zeile mit Index 5
#         df.loc[index, 'Calories'] = 45 # wir ändern den Wert in der Zeile mit Index 5 in der Spalte 'Calories'

# print(df.to_string) """
df.to_excel("data1_new.xlsx") # wir speichern den DataFrame in einer Excel-Datei


