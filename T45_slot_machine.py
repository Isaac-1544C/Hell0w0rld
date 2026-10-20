import random

def spin_row():
    symbols = ['A', 'B', 'C', 'D', 'E']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == 'A':
            return bet * 3
        elif row[0] == 'B':
            return bet * 4
        elif row[0] == 'C':
            return bet * 5
        elif row[0] == 'D':
            return bet * 10
        elif row[0] == 'E':
            return bet * 2000
    return 0

def main():
    balance = 100

    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols: A B C D E")
    print("*************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("That's not a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again == 'N':
            break
        elif play_again != 'Y':
            print("invalid, continue")
        else:
            print("continue")

    print("*******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("*******************************************")

if __name__ == '__main__':
    main()

#normal: 50, Y, 49, N
#abnormal: s, 114514, -1000, 56.22, 10, k
#extreme: 100