# Liste des mois
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        try:
            # Demander la date à l'utilisateur
            date = input("Date: ")
            # Vérifier si la date contient un slash (format MM/DD/YYYY)
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)            
            # Sinon, c'est le format "Month Day, Year"
            else:
                # Vérifier qu'il y a une virgule
                if "," not in date:
                    continue
                # Séparer par la virgule
                parts = date.split(",")
                # Extraire le mois et le jour de la première partie
                month_day = parts[0].strip().split(" ")     
                if len(month_day) != 2:
                    continue
                month_name = month_day[0]
                day = int(month_day[1])
                # Extraire l'année
                year = int(parts[1].strip())
                # Convertir le nom du mois en numéro
                if month_name not in months:
                    continue
                month = months.index(month_name) + 1
            # Vérifier que le mois est valide (1-12)
            if month < 1 or month > 12:
                continue
            # Vérifier que le jour est valide (1-31)
            if day < 1 or day > 31:
                continue
            # Afficher la date au format ISO 8601
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break  
        except (ValueError, IndexError):
            # Si une erreur se produit, redemander
            pass
        except EOFError:
            # Si l'utilisateur appuie sur Ctrl+D (ou Ctrl+Z sur Windows), quitter le programme
            break

main()