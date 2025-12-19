# Menu de taqueria
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0.0
    
    while True:
        try:
            # Demander l'item au user et le convertir en TitleCase pour éviter la casse
            item = input("Item: ").title()
            
            # Vérifier si l'item est dans le menu
            if item in menu:
                # Ajouter le prix de l'item au total
                total += menu[item]
                # Afficher le total actuel avec 2 décimales
                print(f"Total: ${total:.2f}")
            else:
                # Lever une ValueError si l'item n'est pas dans le menu
                raise ValueError(f"'{item}' n'est pas dans le menu")
                
        except ValueError as e:
            # Afficher le message d'erreur et continuer
            print(f"Erreur: {e}")
            
        except EOFError:
            # L'utilisateur a pressé Control-D (ou Control-Z sur Windows)
            # Nouvelle ligne pour une meilleure présentation
            print()
            # Sortir de la boucle
            break

main()