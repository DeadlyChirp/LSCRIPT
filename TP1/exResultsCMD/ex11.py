# imprimer chaque caractere

s = "Hello, World!"
for c in s:
    print(c)



# imprimer uniquement les voyelles

s = "Hello, World!"
vowels = 'aeiouAEIOU'  # Inclut les voyelles majuscules et minuscules
for c in s:
    if c in vowels:
        print(c)

# Exemple d'Utilisation de range()

# Imprimer les nombres de 0 à 4
for i in range(5):
    print(i)

# Imprimer les nombres de 1 à 4
for i in range(1, 5):
    print(i)

# Imprimer les nombres pairs entre 0 et 10 (inclus)
for i in range(0, 11, 2):
    print(i)
