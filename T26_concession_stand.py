menu = {"rice": 3.00,
        "apple": 4.50,
        "bear": 6.00,
        "banananananana": 2.50,
        "orange": 1.00,
        "watermelon": 3.50,
        "pineapple": 3.00,
        "water": 4.25}
#dict
cart = []
total = 0

print("menu:")
for key, value in menu.items():
    #double traverse
    print(f"{key:10}: ${value:.2f}")
print('\n')

while True:
    food = input("Select an item (q to quit): ").lower()
    #ensure it's in lowercase
    if food == "q":
        break
    elif menu.get(food) is not None:
        #ensure food exists
        cart.append(food)

print("Your order:")
for food in cart:
    total += menu.get(food)
    #sum prices
    print(food, end=" ")

print('\n')
print(f"Total is: ${total:.2f}")