price = 50
accepted_coins = [25, 10, 5]
total = 0

while total < price:
    amount_due = price - total
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin in accepted_coins:
        total += coin
change = total - price
print(f"Change Owed: {change}")