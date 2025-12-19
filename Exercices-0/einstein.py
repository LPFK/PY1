C = 300000000
M = int(input("Enter a mass : "))
E = M * C ** 2
print(E)

# or we can do it like this to have it scoped in its own little world :

def einstein():
    C = 300000000
    M = int(input("Enter a mass : "))
    E = M * C ** 2
    print(E)

einstein()