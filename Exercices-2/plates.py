def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
#Pas de ponctuation, espaces ou caractères spéciaux

    if not s.isalnum():
        return False
#Vérifier les chiffres

    found_digit = False
    for i, char in enumerate(s):
        if char.isdigit():
#Le premier chiffre ne peut pas être '0'
            if not found_digit and char == '0':
                return False
            found_digit = True
        else:
#Si on a déjà trouvé un chiffre, on ne peut plus avoir de lettres
            if found_digit:
                return False
    return True
if __name__ == "__main__":
    main()