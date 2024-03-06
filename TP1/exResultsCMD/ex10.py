# Demande à l'utilisateur de saisir un entier
nombre = int(input("Veuillez entrer un entier : "))

# Utilisation de l'expression conditionnelle pour déterminer si le nombre est positif, négatif ou zéro
resultat = "positif" if nombre > 0 else ("negatif" if nombre < 0 else "zero")

# Affiche le résultat
print(resultat)
