import pandas as pd
import matplotlib.pyplot as plt
# Bitte noch folgende Module installieren

df = pd.DataFrame({"area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }, 
        index=["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"])
# DataFrame mit Daten zu Fläche und Bevölkerung von Hauptstädten
print(df)

df.to_excel("pd_04_to_excel.xlsx")
# wir speichern den DataFrame in einer Excel-Datei

df.plot(kind = 'bar')
# wir erstellen ein Balkendiagramm aus dem DataFrame
plt.gcf().set_size_inches(10,8)
# wir passen die Größe des Diagramms an

plt.show()
# wir zeigen das Diagramm an

