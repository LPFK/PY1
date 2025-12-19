try:
    x = int(input("What's x : "))
    print(f"x is {x}")
except ValueError:
    print("Your x is not an integer")

# you can do it this way as well with an else  

try:
    y = int(input("What's y : "))
except ValueError:
    print("Your y is not an integer")
else:
    print(f"y is {y}")

while x <= y:
    x += 1
    print(x)




