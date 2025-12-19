#now let's do it with a while loop,
#so we can do it again and again until we get a valid input
while True : 
    try : 
        x = int(input("What's x : "))
    except ValueError : 
        print("x is not an integer")
    else : 
        break
print(f"x is {x}")
