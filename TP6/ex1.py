from pathlib import Path

def listfichNomC(p,nom): #liste tous les fichiers qui se trouvent dans l'arborescence de p et qui contiennent le mot nom
    for file in p.glob('**/*'):
        if file.is_file() and nom in file.name: #is_file() returns True if the path is a file
            print(file.name)


#test ex1
print('ex1 tester : \n')
p = Path('.')
listfichNomC(p,'ex4') # Doit afficher ex1.py


def listfichNomS(p,nom): #liste tous les fichiers qui se trouvent dans l'arboresence de racine p et le nom sans le suffixe est nom
    for file in p.glob('**/*'):
        if file.is_file() and nom in file.stem: #stem is the name without the suffix
            print(file.name)

print('\nex2 tester : \n')
p = Path('.')
listfichNomS(p,'ex1') # Doit afficher ex1.py

def listfichr(p=Path('.'), s=''):
    """Lists all files in the directory tree rooted at 'p' starting with 's'."""
    for file in p.glob(f'**/{s}*'):
        if file.is_file():
            print(file)

print('\nex3 tester : \n')
p = Path('.')
listfichr(p,'ex') # Doit afficher ex1.py, ex2.py, ex3.py, ex4.py, ex5.py, ex6.py, ex7.py, ex8.py, ex9.py
