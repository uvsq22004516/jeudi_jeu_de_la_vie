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

COUL_FOND = "blue"
LARGEUR = 600
HAUTEUR = 400




########################
# fonctions



########################
# programme principal

racine = tk.Tk()
racine.title("Jeu de la vie")
# création des widgets
canvas = tk.Canvas(racine, bg=COUL_FOND, width=LARGEUR, height=HAUTEUR)
# positionnement
canvas.grid()
# boucle principal
racine.mainloop()
