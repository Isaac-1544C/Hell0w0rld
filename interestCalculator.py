
principle = 0.0
while principle <= 0:
    principle = float(input("Enter Priciple:"))
    if principle <= 0:
        print("can't be <= 0, retry:")


rate = 0.0
while rate <= 0:
    rate = float(input("Enter Rate:"))
    if rate <= 0:
        print("can't be <= 0, retry:")

time = 0
while time <= 0:
    time = int(input("Enter time:"))
    if time <= 0:
        print("can't be <= 0, retry:")

print(f"principle: {principle:.2f}\nrate: {rate:.2f}\n time:{time}\n\n")

balance = principle * pow((1 + rate /100), time)

print(f"total: {balance:.6f}")



