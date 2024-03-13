# Dans cet exercice, on demande de définir des fonctions qui prennent en argument un nom de fichier et qui affichent les lignes de ce fichier qui respectent certaines propriétés. 1. filtre1 : afficher les lignes qui commencent par un mot d’au moins 8 et d’au plus 12 caractères alphanumériques.

import re


def filtre1(nomfichier):
    with open(nomfichier) as f:
        p =re.compile(r'\w{8,12}\b')
        for l in f:
            if p.match(l):
                print(l)


#  filtre2 : afficher les lignes qui contiennent le mot toto.
def filtre2(nomfichier):
    with open(nomfichier) as f:
        for line in f:
            if re.search(r'\btoto\b', line):
                print(line)

# filtre3 : afficher les lignes qui contiennent au moins trois fois le mot toto.

def filtre3(nomfichier):
    with open(nomfichier) as f:
       p = re.compile(r'\btoto\b.*\btoto\b.*\btoto\b')
       for l in f :
           if p.match(l):
               print(l)


# filtre4 : afficher les lignes qui contiennent au moins trois fois le même mot sur l’alphabet [a-z].

def filtre4(nomfichier):
    with open(nomfichier) as f:
        p = re.compile(r'\b([a-zA-Z]+)\b.\b\1\b.\b\1\b')  # \1 dit "revoit la mm chose que j'ai parsé"
        for line in f:
            if p.match(line):
                print(line)


#test with ex.txt
print('filtre1')
filtre1('ex.txt')
print('\n')
print('filtre2')
filtre2('ex2.txt')
print('\n')
print('filtre3')
filtre3('ex3.txt')
print('\n')
print('filtre4')
filtre4('ex4.txt')