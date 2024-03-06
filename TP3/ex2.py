def list_to_dict(l):
    """Convertit une liste en dictionnaire où les clés sont les indices."""
    return {i: l[i] for i in range(len(l))}


def chars(w):
    """Crée un dictionnaire avec la fréquence de chaque caractère dans la chaîne."""
    char_count = {}
    for char in w:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_dict(d):
    """Affiche les couples clé-valeur d'un dictionnaire, un par ligne."""
    for key, value in d.items():
        print(f"{key} {value}")


def merge(d1, d2):
    """Fusionne deux dictionnaires en conservant uniquement les clés communes avec les valeurs regroupées en 2-uplets."""
    return {k: (d1[k], d2[k]) for k in d1 if k in d2}


def inverse(d):
    """Retourne le dictionnaire inversé où les clés deviennent les valeurs et vice-versa.
    Si d contient plusieurs occurrences de la même valeur, retourne un dictionnaire vide."""
    inverse_dict = {}
    for key, value in d.items():
        if value in inverse_dict:
            # Si une valeur est rencontrée plus d'une fois, retourne un dictionnaire vide
            return {}
        else:
            inverse_dict[value] = key
    return inverse_dict


# Exemple d'utilisation de la fonction list_to_dict
print(list_to_dict([1, 2, 3, 4, 5]))  # Devrait afficher {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
print(list_to_dict(["petit", "klein", "small"]))  # Doit retourner {0: 'petit', 1: 'klein', 2: 'small'}

example_dict = chars("aacababbcc")
print_dict(example_dict)  # Doit afficher le nombre d'occurrences de chaque caractère


# Exemple d'utilisation de la fonction merge
'''d1 est {'r': 0.56, 't': 0.78, 'i': 0.23, 'u': 0.35}.
d2 est {'i': 5, 'v': 89, 'p': 65, 't': 21, 'b': 55}.'''
d1 = {'r': 0.56, 't': 0.78, 'i': 0.23, 'u': 0.35}
d2 = {'i': 5, 'v': 89, 'p': 65, 't': 21, 'b': 55}
print(merge(d1, d2))  # Devrait afficher {'i': (0.23, 5), 't': (0.78, 21)}


# Exemples d'utilisation de la fonction inverse
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 2}  # Contient des valeurs dupliquées

# Affichage des résultats
print(inverse(d1))  # Doit afficher {1: 'a', 2: 'b', 3: 'c'}
print(inverse(d2))  # Doit afficher {}