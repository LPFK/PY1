import sys
import requests

def main():
    # Vérifier qu'il y a exactement un argument
    if len(sys.argv) != 2:
        sys.exit("Usage: python team_rocket.py <number_of_pikachus>")
    
    # Vérifier que l'argument est un entier positif
    try:
        n = int(sys.argv[1])
        if n <= 0:
            sys.exit("Error: You cannot have a negative or zero number of Pikachus! Please enter a positive whole number.")
    except ValueError:
        sys.exit("Error: You cannot have a fraction of a Pikachu! Please enter a whole number.")
    
    # Obtenir le poids d'un Pikachu
    try:
        pikachu_weight_kg = get_pikachu_weight()
    except requests.RequestException:
        sys.exit("Error: Unable to connect to PokeAPI. Please check your internet connection.")
    
    # Calculer le poids total
    total_weight = pikachu_weight_kg * n
    
    # Afficher le résultat avec 4 décimales
    print(f"Total weight: {total_weight:.4f} kg")

def get_pikachu_weight():
    """Récupère le poids d'un Pikachu depuis l'API PokeAPI"""
    # URL de l'API pour Pikachu
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    
    # Faire la requête à l'API
    response = requests.get(url)
    
    # Vérifier que la requête a réussi
    response.raise_for_status()
    
    # Extraire les données JSON
    data = response.json()
    
    # Récupérer le poids en hectogrammes
    weight_hectograms = data["weight"]
    
    # Convertir en kilogrammes (1 hectogramme = 0.1 kg)
    weight_kg = weight_hectograms / 10
    
    return weight_kg

if __name__ == "__main__":
    main()