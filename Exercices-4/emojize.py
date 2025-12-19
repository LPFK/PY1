import emoji

def main():
    # Demander une chaîne de texte à l'utilisateur
    text = input("Input: ")
    # Convertir les alias en émojis
    result = emoji.emojize(text, language='alias')

    # Afficher le résultat
    print(f"Output: {result}")

main()