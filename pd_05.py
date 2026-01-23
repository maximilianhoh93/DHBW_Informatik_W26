
import pandas as pd
import matplotlib.pyplot as plt

# Bitte noch folgende Module installieren
# pip install matplotlib
# pip install openpyxl

'''
df = pd.DataFrame({'length': [1.5, 0.5, 1.2, 0.9, 3],
                  'width': [0.7, 0.2, 0.15, 0.2, 1.1]},
                  index=['pig', 'rabbit', 'duck', 'chicken', 'horse'])
'''

df = pd.read_excel("pd05_data.xlsx")
# DataFrame mit Daten zu verschiedenen Städten
print(df)
# wir lesen die Daten aus einer Excel-Datei ein
df=df.set_index("Town")
# wir setzen die Spalte "Town" als Index

print(df)
# wir geben den DataFrame aus

plot = df.plot(title="Town Data",kind = 'bar')
#plot = df.plot(title="Town Data",kind = 'line')
plt.gcf().set_size_inches(10,8)

plt.savefig('pd_05_Town_Data.jpg', dpi=200)
plt.show()
