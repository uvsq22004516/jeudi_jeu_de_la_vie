####################################################
# Auteurs:
# Pierre Coucheney
# Toto
# Groupe:
# MPCI 2
# dépot Github:
# https://github.com/coucheney/jeudi_jeu_de_la_vie
###################################################

#########################
# import des modules

import tkinter as tk
import copy

##########################
# constantes

COUL_FOND = "grey20"
COULEUR_QUADR = "grey60"
COULEUR_VIVANT = "yellow"
LARGEUR = 600
HAUTEUR = 400
COTE = 20
NB_COL = LARGEUR // COTE
NB_LIG = HAUTEUR // COTE

#########################
# variables globales

tableau = None

########################
# fonctions

def quadrillage():
    """Affiche un quadrillage constitué de carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    x = 0
    while x <= LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        x += COTE



def xy_to_ij(x, y):
    """Retourne la colonne et la ligne du tableau correspondant aux coordonnées (x,y) du canevas"""
    # A FAIRE
    return x // COTE, y // COTE


def chg_case(event):
    """Modifier l'état de la case aux coordonnées (event.x, event.y)"""
    i, j = xy_to_ij(event.x, event.y)
    if tableau[i][j] > 0:
        # si case vivante
        canvas.delete(tableau[i][j])
        tableau[i][j] = 0
    else:
        # si case morte
        x, y = COTE * i, COTE * j
        carre = canvas.create_rectangle((x, y),(x + COTE, y + COTE), fill=COULEUR_VIVANT, outline=COULEUR_QUADR)
        tableau[i][j] = carre


def nb_vivant(i, j):
    """Retourne le nombre de cases vivantes autour de la case de coordonnées (i, j)"""
    pass


def traite_case(i, j):
    """Fait une étape de l'automate pour la case de coordonnées (i, j) 
    en retournant la nouvelle valeur de la case du tableau"""
    pass


def etape():
    """Fait une étape du jeu de la vie en modifiant la variable globale tableau"""
    tableau_res = copy.deepcopy(tableau)
    for i in range(NB_COL):
        for j in range(NB_LIG):
            traite_case(i, j)
    tableau = tableau_res



########################
# programme principal

tableau = []
for i in range(NB_COL):
    tableau.append([0] * NB_LIG)


racine = tk.Tk()
racine.title("Jeu de la vie")
# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR)

# positionnement
canvas.grid()

# gestion des événements
canvas.bind("<Button-1>", chg_case)

# autres fonctions
quadrillage()

# boucle principal
racine.mainloop()
