#exo1 

import random
import re


def Deviner(k):
    n = random.randint(0, k)
    a = 0
    while a != n:
        try:
            a= int(input("Entrez un nombre: "))
            if a < n:
                print("Trop petit")
            elif a > n:
                print("Trop grand")
            elif a == n:
                print("Bravo!")
        except ValueError:
            print("Proposez uniquement des nombres entiers")
        except KeyboardInterrupt:
            print("\nle nombre était :", n)
            break               
    print("Au revoir!")

#Deviner(100)
    
#exo2
    
def frequence(nomfichier):
    with open(nomfichier) as f:
        s = f.read().lower()
        words = re.findall(r'\b\w+\b', s)
        word_counts = {}
        for word in words:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
        most_common_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:5]
        return most_common_words
        
    
print(frequence("CMTP4/proust.txt"))


def frequence(nomfich, n=5):
    # Ouvrir le fichier et lire son contenu
    with open(nomfich, 'r', encoding='utf-8') as f:
        texte = f.read().lower()  # Convertir en minuscules pour éviter la sensibilité à la casse

    # Utiliser une expression régulière pour extraire tous les mots du texte
    mots = re.findall(r'\b\w+\b', texte)

    # Initialiser un dictionnaire pour compter la fréquence de chaque mot
    compteur = {}

    # Remplir le dictionnaire avec la fréquence de chaque mot,
    # mais seulement pour les mots dont la longueur est strictement supérieure à n
    for mot in mots:
        if len(mot) > n:
            if mot not in compteur:
                compteur[mot] = 1
            else:
                compteur[mot] += 1

    # Trier le dictionnaire par valeur (fréquence) dans l'ordre décroissant
    mots_les_plus_frequents = sorted(compteur.items(), key=lambda x: x[1], reverse=True)[:5]

    # Afficher les mots les plus fréquents
    for mot, frequence in mots_les_plus_frequents:
        print(mot, frequence)

# Exemple d'utilisation :
# frequence("proust.txt", 6)