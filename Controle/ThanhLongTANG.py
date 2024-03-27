

#ex1
def chaine(s):
    return s.isdigit()

# Exemples d'utilisation
print('\nex1 exemple')
print(chaine('9821739812073981279381'))
print(chaine('tot5'))


#ex2
def aux(L):
    return [x for x in L if x%2==0]

L=[56,7,-4,8,23,-89,101,78]
print('\nex2 exemple')
print(aux(L))

#ex3
def sous_liste(L, k1, k2):
    return [x for x in L if k1 <= x <= k2]

# Exemple d'utilisation
L = [56, 7, 27, 4, 8, 23, 89, 101, 78, 45, 3, 18, 9]
print('\nex3 exemple')
print(sous_liste(L, 10, 40))  # Doit afficher [27, 23, 18]


#ex4
def zzz(L1,L2):
    result=[]
    for item1,item2 in zip(L1,L2):
        result.append(item1)
        result.append(item2)
    return result

L1=[78,101,89,23,8,4,7,56]
L2=[-2,-4,-1,-90,-7,-5,-3,-2]
print('\nex4 exemple')
print(zzz(L1,L2))
#doit afficher [78,-2,101,-4,89,-1,23,-90,8,-7,4,-5,7,-3,56,-2] ]


#ex5
def triAbsDecr(L):
    return sorted(L, key=lambda x: abs(x), reverse=True)


L = [5, -78, -4, 7, 9]
print('\nex5 exemple')
print(triAbsDecr(L))  # Doit afficher [-78, 9, 7, 5, -4]



#ex6
def verifDico(d):
    valeurs_vues = set()
    for valeur in d.values():
        if valeur in valeurs_vues:
            return True
        valeurs_vues.add(valeur)
    return False

d={4:67,5:8,67:24,78:56,89:34,22:3}
print('\nex6 exemple')
print(verifDico(d))  # Doit afficher false
print('\n2eme exemple')
d={4:67,5:8,67:3,78:56,89:34,22:3}
print(verifDico(d))  # Doit afficher true



#ex7
def Nblignes(nom):
    with open(nom, 'r') as fichier:
        for ligne in fichier:
            if 'bip' in ligne:
                print(ligne.strip())


print('\nex7 exemple')
Nblignes('toto.txt')


#ex8
import re

def Nblignes(nom):
    with open(nom, 'r') as fichier:
        for ligne in fichier:
            occurrences = re.findall(r'\bbip\b', ligne)
            if len(occurrences) == 2:
                print(ligne.strip())

# Exemple d'utilisation
print('\nex8 exemple')
Nblignes('toto.txt')


#ex9

print('\nex9 exemple')
print('launching the game...')

import random



def newListe(n): #qui construit une liste de n entiers aléatoires compris entre -100 et 100.
    return [random.randint(-100, 100) for _ in range(n)]


def ChoixOrdi(L, dejaelim):
    if not dejaelim:
        return 'E' + str(random.randint(0, len(L) - 1))
    else:
        if L[0] > L[-1]:
            return 'G'
        else:
            return 'D'




def gagne(L1, L2):
    if sum(L1) > sum(L2):
        print("Player 1 wins!")
    elif sum(L2) > sum(L1):
        print("Player 2 (Computer) wins!")
    else:
        print("It's a tie!")

def displayCartes(L):
    cards_with_indexes = [f"{value} (i: {index})" for index, value in enumerate(L)]
    print("Cards on the table:", ", ".join(cards_with_indexes))


def Cartes(n):
    try:
        L = newListe(n)
        player_cards, computer_cards = [], []
        player_elim, computer_elim = False, False

        displayCartes(L)
        player_starts = input("Do you want to start the game? (yes/no): ").lower().strip() == 'yes'

        while L:
            if player_starts or not L:
                while True:
                    elim_prompt = " or an index to eliminate (1 time only)" if not player_elim else ""
                    move = input(f"Choose your move (G for left, D for right{elim_prompt}, or R to redo): ").strip()

                    if move.upper() == 'R':
                        print("Redoing move. Please choose again.")
                        continue

                    if move.upper() in ['G', 'D'] or (move.isdigit() and not player_elim):
                        if move.upper() == 'G':
                            player_cards.append(L.pop(0))
                        elif move.upper() == 'D':
                            player_cards.append(L.pop(-1))
                        elif move.isdigit():
                            index = int(move)
                            if 0 <= index < len(L):
                                L.pop(index)
                                player_elim = True
                        displayCartes(L)
                        break

                    else:
                        print("Invalid move or you already eliminated a card. Try again.")
                        displayCartes(L)


            if L:
                computer_move = ChoixOrdi(L, computer_elim)
                if computer_move.startswith('E') and not computer_elim:
                    _, index = computer_move[0], int(computer_move[1:])
                    print("Computer eliminates card at index:", index)
                    L.pop(index)
                    computer_elim = True
                elif computer_move == 'G':
                    print("Computer takes:", L[0])
                    computer_cards.append(L.pop(0))
                elif computer_move == 'D':
                    print("Computer takes:", L[-1])
                    computer_cards.append(L.pop(-1))
                displayCartes(L)

            player_starts = not player_starts

        gagne(player_cards, computer_cards)

    except KeyboardInterrupt:
        print("\nJeu interrompu par l'utilisateur. Fin du jeu.")


def startGame():
    try:
        n = int(input("How many cards do you want to start with? "))
        Cartes(n)
    except ValueError:
        print("Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nGame interrupted by the user. Exiting...")
if __name__ == "__main__":
            startGame()