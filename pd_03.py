import pandas as pd
# Bitte noch folgende Module installieren
# pip install matplotlib
# pip install openpyxl

df = pd.read_csv('data_dup.csv')
print(df)
# wir schauen nach, ob es Duplikate gibt

x = df["Calories"].mode()[0]
# mode() gibt den am häufigsten vorkommenden Wert zurück
# die 0 bedeutet, dass wir den ersten Wert nehmen, falls es mehrere gibt

df["Calories"].fillna(x, inplace = True)
# wir füllen die NaN-Werte in der Spalte "Calories" mit dem Modus auf
# die Lücken werden also mit dem am häufigsten vorkommenden Wert gefüllt

print(df.to_string())
# wir geben den gesamten DataFrame aus, auch wenn er sehr groß ist

