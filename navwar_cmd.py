# On importe la fonction randint du module random
from random import randint

# On déclare notre grille ici pour qu'elle soit visible dans l'ensemble du programme.
board = []


def initialise():
    # On ajoute 10 listes de 10 éléments '-' dans notre liste board
    for x in range(10):
        board.append(['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])


def printboard(mode):
    print("")
    print("*" * 10 + ' Board ' + "*" * 10)
    print("*" + ' ' * 25 + "*")
    print("*    0 1 2 3 4 5 6 7 8 9  *")

    # On parcourt la grille
    # On affiche élément par élément sans retour à la ligne
    # à chaque fin de ligne, on fait un print sans end='' pour forcer un retour à la ligne.
    # si le mode est 1 et qu'on trouve une case bateau, alors on affiche un '-' à la place.
    for x in range(10):
        print("*  " + str(x) + " ", end="")

        for y in range(10):
            if mode == 1 and board[x][y] in ('1', '2', '3', '4', '5'):
                print("- ", end="")
            else:
                print(board[x][y] + ' ', end="")

        print(" *")

    print("*" + ' ' * 25 + "*")
    print("*" * 27)


def place(size):
    # Un nombre aléatoire entre 0 et 1 pour choisir l'orientation du bateau.
    orientation = randint(0, 1)
    # Un nombre aléatoire pour la première case du bateau
    start = randint(0, 10 - size)
    # Un nombre aléatoire pour choisir la ligne en cas de bateau horizontal
    # ou la colonne pour un bateau vertical
    position = randint(0, 9)

    # Si le bateau est horizontal (orientation à 0)
    # alors on le place (cad on affecte son nombre (sa taille) dans la grille)
    # la ligne restant la même et pour valeur POSITION (entre 0 et 9)
    # la colonne incrémentée de 1 autant de fois que la taille du bateau
    if orientation == 0:
        for x in range(size):
            board[position][start + x] = str(size)
    # Si le bateau est vertical (orientation à 1)
    # alors on le place (cad on affecte son nombre (sa taille) dans la grille)
    # la colonne restant la même et pour valeur POSITION (entre 0 et 9)
    # la ligne incrémentée de 1 autant de fois que la taille du bateau
    else:
        for x in range(size):
            board[start + x][position] = str(size)


def shoot(row, col):
    # SI la case contient un nombre cad un bateau,
    # alors on affiche "touché" et on place un 'X' à la place
    if board[row][col] in ('1', '2', '3', '4', '5'):
        print("Touché en (%i,%i)" % (row, col))
        board[row][col] = 'X'
    # SINON SI la case contient un 'X' ou un '0' alors la case
    # a déjà été jouée et on retourne 0
    elif board[row][col] == 'X' or board[row][col] == '0':
        return 0
    # SINON on place un '0' dans la case
    else:
        board[row][col] = '0'

    return 1


def checkboard():
    # On parcourt notre grille, si on trouve un nombre en 1 et 5 alors
    # on retourne 0 qui signifie que l'on a trouvé un bateau
    for x in range(10):
        for y in range(10):
            if board[x][y] in ('1', '2', '3', '4', '5'):
                return 0
    # à la fin du parcours de la grille, si le programme arrive ici
    # On n'a donc jamais retourné 0 et donc jamais trouvé de case bateau
    # alors on retourne 1 pour signifier que le jeu est gagné
    return 1


#######################
# début du programme
#######################

# On appelle la fonction pour initialiser la grille
initialise()
# On appelle la fonction pour placer un bateau de taille 5 dans la grille
place(5)
#  On initialise un compteur pour le nombre de coups
coups = 0
# Pour tricher un peu si besoin
# printboard(0)

# Tant que la fonction de vérification dit que le jeu n'est pas terminé
while checkboard() == 0:
    #  On affiche la grille sans les bateaux
    printboard(1)

    # On fait saisir une ligne et une colonne
    r = int(input("saisir une ligne: "))
    while r not in range(10):
        r = int(input("saisir une ligne valide: "))

    c = int(input("saisir une colonne: "))
    while c not in range(10):
        c = int(input("saisir une colonne valide: "))

    if shoot(r, c) == 0:
        print("Case déjà jouée !!")
        # Si on a déjà joué une case, on passe directement à la prochaine occurrence de la boucle
        # grâce au mot clé continue
        continue

    coups += 1

printboard(1)
print("Vous avez gagné en %i coups" % coups)
