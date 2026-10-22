principle = 0.0
while principle <= 0:
    principle = float(input("Enter Principle:"))
    #input principle
    if principle <= 0:
    #make sure > 0
        print("can't be <= 0")


rate = 0.0
while rate <= 0:
    rate = float(input("Enter Rate:"))
    #input rate
    if rate <= 0:
    #make sure > 0
        print("can't be <= 0")
    

time = 0
while time <= 0:
    time = int(input("Enter Time:"))
    #input time
    if time <= 0:
    #make sure > 0  
        print("can't be <= 0")

print(f"principle: {principle:.2f}\nrate: {rate:.2f}\n time:{time}\n\n")

balance = principle * pow((1 + rate /100), time)
#calculate pv*(1+r)^n

print(f"total: {balance:.6f}")
#output



