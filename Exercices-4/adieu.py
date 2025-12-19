import inflect

def main():
    # Créer une instance de inflect
    p = inflect.engine()
    # Liste pour stocker les noms
    names = []
    print("Enter names (press Ctrl-Z to finish):")
    
    try:
        while True:
            # Demander un nom à l'utilisateur
            name = input("Name: ")
            # Ajouter le nom à la liste
            names.append(name)
    except EOFError:
        # L'utilisateur a pressé Control-D (ou Control-Z sur Windows)
        pass
    
    # Afficher le message d'adieu
    if names:
        # Utiliser inflect pour joindre les noms correctement
        formatted_names = p.join(names)
        print(f"\nAdieu, adieu, to {formatted_names}")

main()