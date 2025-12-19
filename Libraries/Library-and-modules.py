# documentation : https://docs.python.org/3/library/random.html
import random 

coin = random.randint(0, 1)

if coin == 0:
    print("Tails")
else:
    print("Heads")

coin2 = random.choice(["Face", "Pile"])
print(coin2)