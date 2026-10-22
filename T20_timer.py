import time

set_time = int(input("input time in second:\n"))
#time to be counted down

for x in range(set_time, 0, -1):
    seconds = x % 60
    minutes = (x // 60) % 60
    #0 <= minutes <= 60
    hours = x // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    #delay 1s
        
print("time's up")