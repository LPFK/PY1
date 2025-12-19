# figlet.py

import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    # Obtenir la liste de toutes les polices disponibles
    available_fonts = figlet.getFonts()
    # Vérifier les arguments de ligne de commande
    if len(sys.argv) == 1:
        # Aucun argument : choisir une police aléatoire
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3:
        # Deux arguments : vérifier le flag et la police
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")  
        font = sys.argv[2] 
        # Vérifier si la police existe
        if font not in available_fonts:
            sys.exit("Invalid usage")
    else:
        # Nombre d'arguments incorrect
        sys.exit("Invalid usage")
    # Définir la police
    figlet.setFont(font=font)
    # Demander le texte à l'utilisateur
    text = input("Input: ")
    # Afficher le texte en art ASCII
    print(figlet.renderText(text))

main()