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

##########################
# constantes

COUL_FOND = "grey20"
COULEUR_QUADR = "grey60"
LARGEUR = 600
HAUTEUR = 400
COTE = 10

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



def xy_to_cl(x, y):
    """Retourne la colonne et la ligne du tableau correspondant aux coordonnées (x,y) du canevas"""
    # A FAIRE
    return 0, 0


def chg_case(event):
    """Modifier l'état de la case aux coordonnées (event.x, event.y)"""
    c, l = xy_to_cl(event.x, event.y)
    if tableau[c][l] >= 0:
        # si case vivante
        canvas.delete(tableau[c][l])
        tableau[c][l] = -1
    else:
        # si case morte
        carre = canvas.create_rectangle((0,0),(COTE,COTE), fill=COULEUR_VIVANT)
        tableau[c][l] = carre




########################
# programme principal

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
