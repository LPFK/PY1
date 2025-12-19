import random
def main():
    # obtenir le niveau et initialiser le score
    level = get_level()
    score = 0
    # generer 10 problemes
    for _ in range(10):
        # generer selon le niveau choisi
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        # user n'a que 3 try
        attempts = 0
        while attempts < 3:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct_answer:
                    score += 1
                    break
                else:
                    attempts += 1
                    print("EEE")
            except ValueError:
                print("EEE")
                attempts += 1
                # si 3 erreurs, afficher la reponse
        if attempts == 3:
            print(f"{x} + {y} = {correct_answer}")
    # afficher le score final
    print(f"Score: {score}")
        
def get_level():
    # demande un niveau valide entre 1, 2 et 3
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass
def generate_integer(level):
    # genere un entier aleatoire selon le niveau

    # lvl 1 : 0-9
    if level == 1:
        return random.randint(0, 9)
    # lvl 2 : 10-99
    elif level == 2:
        return random.randint(10, 99)
    # lvl 3 : 100-999
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()