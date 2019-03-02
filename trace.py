import numpy as np
import matplotlib.pyplot as plt

results = []

# Lecture de notre fichier
with open("results.txt", "r") as f:
    for x in f.readlines():
        results.append(x.split("\n")[0])

results = np.array(results, dtype="float64") # Conversion de la liste en matrice numpy de type float64

plt.plot(results) # Ecriture des données
plt.show() # Affichage des données