def is_balanced(s):
    # Utilise une pile pour garder une trace des parenthèses ouvrantes rencontrées
    stack = []
    # Dictionnaire pour correspondre les parenthèses ouvrantes avec leurs fermantes
    brackets = {')': '(', ']': '['}

    # Parcours de la chaîne de caractères
    for char in s:
        # Si on rencontre une parenthèse ouvrante, on l'ajoute à la pile
        if char in brackets.values():
            stack.append(char)
        # Si on rencontre une parenthèse fermante
        elif char in brackets:
            # Si la pile est vide ou que la parenthèse ouvrante au sommet de la pile ne correspond pas
            # à la parenthèse fermante rencontrée, les parenthèses ne sont pas équilibrées
            if not stack or stack.pop() != brackets[char]:
                return False
    # Si la pile est vide, toutes les parenthèses ouvrantes ont été fermées
    return not stack


# Tests de la fonction is_balanced
print(is_balanced("([aa](bb[]))"))  # Doit retourner True
print(is_balanced("([aa)](bb[])"))  # Doit retourner False
print(is_balanced("([aa](bb[])"))  # Doit retourner False
print(is_balanced("([])[]()"))  # Doit retourner True
print(is_balanced("([)]"))  # Doit retourner False
print(is_balanced("((()))[()]"))  # Doit retourner True
print(is_balanced("((())"))  # Doit retourner False
print(is_balanced("(()))"))  # Doit retourner False
