import random

def main():
    # demander le niveau
    level = get_level()

    # generer un nombre aleatoire entre 1 et level
    secret_number = random.randint(1, level)
    # Boucle de devinettes
    while True:
        guess = get_guess()
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_level():
    #Demande un niveau valide à l'utilisateur
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def get_guess():
    #Demande une devinette valide à l'utilisateur
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass

if __name__ == "__main__":
    main()