x = float(input("Enter a number: "))
#ici x a un scope global
def add(nombre):
    y = 2
    print(x + y)
    #ici y a un scope local unique a la fonction add

add(x)

x = float(input("Enter a number: "))
#ici x a un scope global
def add(nombre):
    return nombre + 2
    #ici y a un scope local unique a la fonction add

print(add(x) % 3)