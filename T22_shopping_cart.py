foods = []
prices = []
total = 0

while 1:
    food = input("Enter a food to buy (q to quit): \n")
    if food.lower() == 'q':
        break
    price = float(input(f"Enter the price of a {food}: $"))
    foods.append(food)
    prices.append(price)

print("--your cart--")

for food in foods:
    print(food, end=" ")

print('\n')

for price in prices:
    total += price

print(f"your total is: {total}$")
