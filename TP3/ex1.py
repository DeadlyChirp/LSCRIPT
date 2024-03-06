'''same_element(l1,l2) qui renvoie true si les lites l1 et l2 contiennent les memes elements dans le meme ordre et false sinon'''

def same_elements(l1, l2):
    """Renvoie True si les listes l1 et l2 contiennent les mêmes éléments, False sinon."""
    for x in l1:
        if x not in l2: return False
    for x in l2:
        if x not in l1: return False
    return True

def letters():
    user_input = input("Entrez une ligne de texte : ")
    letters_set = {char.lower() for char in user_input if char.isalpha()}
    return letters_set

def to_list(s):
    """Prend un ensemble d'entiers et renvoie une liste triée de ces entiers."""
    return sorted(list(s))


def even(s):
    """Prend un ensemble d'entiers et renvoie un ensemble des nombres pairs."""
    return {x for x in s if x % 2 == 0}

print('question1')
# Exemple d'utilisation de la fonction same_elements
print(same_elements([1, 2, 3, 2], [3, 2, 1, 2]))  # Devrait afficher True
print(same_elements([1, 2, 3], [3, 2, 4]))        # Devrait afficher False
print('question2')
print(letters())  # Exemple d'utilisation de la fonction letters
print('question3')
# Exemple d'utilisation de la fonction to_list
print(to_list({1, 3, 2, 5, 4}))  # Devrait afficher [1, 2, 3, 4, 5]
print('question4')
# Exemple d'utilisation de la fonction even
print(even({1, 2, 3, 4, 5, 6}))  # Devrait afficher {2, 4, 6}