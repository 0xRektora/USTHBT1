import numpy as np
import matplotlib.pyplot as plt

values = np.linspace(10**-16, 10**-15, 1001) # Génération des valeurs

myFunc = lambda x: ((1 + x)-1) / (1 + (x-1)) # Création de notre fonction F(x)
myFunc = np.vectorize(myFunc) # Vectorisation avec numpy de notre fonction pour optimiser le mappage (fonction/valeur)

points = myFunc(values) # Génération de nos points F(x)

# Enregistrement de nos points dans un fichier txt 
with open("results.txt", "w") as f:
    for x in points:
        f.writelines(str(x)+"\n")

