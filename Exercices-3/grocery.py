def main():
    # Dictionnaire pour compter les occurrences de chaque article
    grocery_list = {}


    while True:
        try:
            # Demander l'item au user et le convertir en majuscule
            item = input("Item: ").upper()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            # L'utilisateur a pressé Control-D (ou Control-Z sur Windows)
            # Nouvelle ligne pour une meilleure présentation
            print()
            # Sortir de la boucle
            break
    # Trier la liste par ordre alphabétique
    sorted_items = sorted(grocery_list.keys())
    # Afficher la liste avec les comptes
    for item in sorted_items:
        count = grocery_list[item]
        print(f"{count} {item}")

main()


   