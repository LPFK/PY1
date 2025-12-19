"""Boucle while
Répéter un bloc de code tant qu'une condition est vraie.
Boucle for
Itérer sur une séquence (par exemple, des nombres générés par range).
for avec else
Le bloc else s'exécute si la boucle se termine sans rencontrer de break."""

i = 3
while i < 5:
    print(i)
    i += 1
else:
    print("i is no longer less than 5")

for i in range(1, 11): 

    print(f"5 x {i} = {5*i}")

thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 
print(thisdict)
print(len(thisdict))
print(type(thisdict)) 