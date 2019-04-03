import matplotlib.pyplot as plt
import numpy as npy

stimmen = [14658515, 9990488, 6316080, 4643272, 5155933, 2606902]
parteien = ["CDU/CSU", "SPD", "FDP", "GRUENE", "DIE LINKE", "Sonstige"]
colors = ['c', 'm', 'r', 'g', 'b', 'y']
# plt.pie(stimmen, labels=parteien) # automatic colors
plt.pie(stimmen,
        labels=parteien,
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0, 0, 0, 0, 0, 0.1), # push out a piece of the pie
        autopct='%1.1f%%') # show percentages
plt.title('Bundestagswahl 2009')
plt.show()
