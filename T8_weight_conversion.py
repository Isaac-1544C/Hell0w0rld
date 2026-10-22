while 1:
    try:
        weight = float(input("Enter your weight:\n"))
        #input weight
        break
    except ValueError:
        #if not valid input
        print(f"not valid input")

while 1:
    unit = input("kg:K, Pounds:L\n")
    #input unit
    if unit == 'K':
        #Kgs2Lbs
        weight *= 2.205
        print(f"Your weight: {round(weight, 1)}Lbs.")
        break
    elif unit == 'L':
        #Lbs2Kgs
        weight /= 2.205
        print(f"Your weight: {round(weight, 1)}Kgs.")
        break
    else:
        #invalid input
        print(f"{unit} was not valid")