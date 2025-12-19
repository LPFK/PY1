import sys 
import requests

def main():
    print("=" * 60)
    print("🚀 TEAM ROCKET - A BALLOON CARGO CALCULATOR 🎈")
    print("=" * 60)
    print("\n")

    while True:
        display_menu()
        choice = input("Enter your choice: ").lower().strip()

        if choice == "1":
            calculate_weight()
        elif choice == "2":
            search_pokemon()
        elif choice == "3":
            list_popular_pokemon()
        elif choice == "4":
            print("Blastin'off again ! Goodbye !")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please select an option between 1, 2, 3 or 4.\n")

def display_menu():
    """Affiche le menu principal"""
    print("\n" + "─" * 60)
    print("📋 MENU:")
    print("─" * 60)
    print("1. Calculate cargo weight for Pokemon capture")
    print("2. Search Pokemon information")
    print("3. List popular Pokemon")
    print("4. Exit")
    print("─" * 60)

def calculate_weight():
    """Calcule le poids total des Pokemon capturés"""
    print("\n" + "=" * 60)
    print("⚖️  CARGO WEIGHT CALCULATOR")
    print("=" * 60)
    print("\n")
    #demander le nom du Pokemon
    pokemon_name = input("\nEnter a Pokemon name: ").strip().lower()
    if not pokemon_name:
        print("\n❌ Pokemon name cannot be empty. Please enter a valid Pokemon name.")
        return
    #demander le nombre de Pokemon
    try:
        pokemon_count = int(input(f"How many {pokemon_name.capitalize()} to capture? "))
        if pokemon_count <= 0:
            print("\n❌ You cannot capture a negative or zero number of Pokemon! Please enter a positive whole number.")
            return
    except ValueError:
        print("\n❌ Invalid input. Please enter a valid number.")
        return
    try:
        pokemon_data = get_pokemon_data(pokemon_name)
    except requests.RequestException as e:
        print(f"\n❌ Unable to connect to the PokeAPI: {e}")
        return
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        return
    # Extraire les informations du Pokemon
    name = pokemon_data["name"].capitalize()
    weight_kg = pokemon_data["weight"] / 10
    height_m = pokemon_data["height"] / 10
    types = [type["type"]["name"] for type in pokemon_data["types"]]
    #calculer le poids total
    total_weight = weight_kg * pokemon_count
    #afficher le resultat
    print("\n" + "─" * 60)
    print(f"📊 POKEMON INFO: {name}")
    print("─" * 60)
    print(f"Type(s): {', '.join(types)}")
    print(f"Height: {height_m:.2f} m")
    print(f"Weight per Pokemon: {weight_kg:.4f} kg")
    print()
    print(f"🎯 Capturing {pokemon_count} {name}(s)...")
    print(f"📦 Total cargo weight: {total_weight:.4f} kg")
    print("─" * 60)

    # evaluation du poids
    if total_weight > 1000:
        print("\n❌ The cargo is too heavy! Please try again with a smaller number of Pokemon.")
        print("   Team Rocket is blasting off again! 💥")
    elif total_weight > 500:
        print("\n⚠️ The cargo is heavy. Be careful during the flight!")
    elif total_weight > 100:
        print("\n⚠️ The cargo is heavy. Be careful during the flight!")
    else:
        print("\n✅ The cargo is light. Team Rocket is ready to blast off!")
        print("   Prepare for trouble, and make it double!")
    print("─" * 60)
    print("\n")
    
def search_pokemon():
    #Recherche des informations sur un Pokemon
    print("\n" + "=" * 60)
    print("🔍 POKEMON SEARCH")
    print("=" * 60)
    print("\n")
    pokemon_name = input("Enter a Pokemon name or ID: ").strip().lower()
    if not pokemon_name:
        print("\n❌ Pokemon name cannot be empty. Please enter a valid Pokemon name.")
        return
    try:
        pokemon_data = get_pokemon_data(pokemon_name)
    except requests.RequestException as e:
        print(f"\n❌ Unable to connect to the PokeAPI: {e}")
        return
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        return
    # Extraire les informations du Pokemon
    pokemon_id = pokemon_data["id"]
    name = pokemon_data["name"].capitalize()
    weight_kg = pokemon_data["weight"] / 10
    height_m = pokemon_data["height"] / 10
    types = [type["type"]["name"] for type in pokemon_data["types"]]
    abilities = [ability["ability"]["name"].capitalize().replace("-", " ")for ability in pokemon_data["abilities"]]
    stats = {stat["stat"]["name"].capitalize(): stat["base_stat"] for stat in pokemon_data["stats"]}
    # Afficher les informations complètes
    print("\n" + "─" * 60)
    print(f"📋 POKEMON PROFILE: {name} (#{pokemon_id})")
    print("─" * 60)
    print(f"Type(s): {', '.join(types)}")
    print(f"Height: {height_m:.2f} m")
    print(f"Weight: {weight_kg:.4f} kg")
    print(f"Abilities: {', '.join(abilities)}")
    print()
    print("📊 BASE STATS:")
    for stat_name, stat_value in stats.items():
        bar = "█" * (stat_value // 10)
        print(f"  {stat_name:15s}: {stat_value:3d} {bar}")
    print("─" * 60)

def list_popular_pokemon():
    # Liste des Pokemon les plus populaires
    print("\n" + "=" * 60)
    print("⭐ POPULAR POKEMON")
    print("=" * 60)

    popular = [
        "pikachu", "charizard", "mewtwo", "bulbasaur", "squirtle",
        "eevee", "snorlax", "gengar", "dragonite", "lucario",
        "charmander", "ivysaur", "arcanine", "venusaur", "mew", "eevee"
    ]
    print("\nHere are some popular Pokemon you can search:")
    print()
    for i, pokemon in enumerate(popular, 1):
        print(f"  {i:2d}. {pokemon.capitalize()}")
    
    print("\n💡 Tip: You can also search by Pokemon ID (e.g., 1, 25, 150)")
    print("─" * 60)

def get_pokemon_data(pokemon_identifier):
    """Récupère les données d'un Pokémon depuis l'API PokeAPI"""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            raise ValueError(f"Pokemon '{pokemon_identifier}' not found!")
        else:
            raise requests.RequestException(f"HTTP Error: {e}")
    except requests.RequestException as e:
        raise requests.RequestException(f"Connection error: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Blasting off again!")
        sys.exit(0)

