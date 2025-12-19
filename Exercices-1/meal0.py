mealtime = input("What time is it? ")
mealtime = mealtime.strip()
mealtime = mealtime.split(":")
if mealtime[0] == "7" or mealtime[0] == "8" or mealtime[0] == "9":
    print("breakfast time")
elif mealtime[0] == "12" or mealtime[0] == "13" or mealtime[0] == "14":
    print("lunch time")
elif mealtime[0] == "18" or mealtime[0] == "19" or mealtime[0] == "20":
    print("dinner time")
else:
    print("no food available right now, not the time for a meal")

