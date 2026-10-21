while 1:
    try:
        weight = float(input("Enter your weight:\n"))
        break
    except ValueError:
        print(f"not valid input")

while 1:
    unit = input("kg:K, Pounds:L\n")
    if unit == 'K':
        weight *= 2.205
        print(f"Your weight: {round(weight, 1)}Lbs.")
        break
    elif unit == 'L':
        weight /= 2.205
        print(f"Your weight: {round(weight, 1)}Kgs.")
        break
    else:
        print(f"{unit} was not valid")