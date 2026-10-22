import random

dice_pic = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0

while 1:
    #prevent invalid input causing valueerror
    num_of_dice = input("how many dice: ")
    if num_of_dice.isdigit():
        num_of_dice = int(num_of_dice)
        break
    else:
        print("invalid")


for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
    #generate n dies

for line in range(5):
    for die in dice:
        print(dice_pic.get(die)[line], end="")
        #print by lines
    print()
    #\n

for die in dice:
    total += die
print(f"total: {total}")