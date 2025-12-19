def main():
    while True:
        try:
            # Demander la fraction au user
            fuel = input("Fraction : ")
            # séparer X et Y avec split
            x, y = fuel.split("/")
            # convertir X et Y en entiers
            x = int(x)
            y = int(y)
            # Vérifier si X est supérieur à Y
            if x > y:
                continue # redemande une entrée
            #calculer le pourcentage de fuel
            percentage = (x / y) * 100
            #arrondir le pourcentage a l'entier le plus proche
            percentage = round(percentage)
            #afficher le résultat selon les regles
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
                #sortir de la boucle avec break
            break
        except ValueError:
            # si X ou Y n'est pas un entier , ou format incorrect
            print("Invalid input. Please enter valid integers for x and y.")
        except ZeroDivisionError:
            # si Y est égal a 0
            print("Invalid input. Please enter valid integers for x and y.")

main()
