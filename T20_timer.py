import time

set_time = int(input("input time in second"))

print(set_time)
last_time = time.time()
while set_time >= 0:
    current_time = time.time()
    if current_time - last_time >= 1:
        last_time = current_time
        set_time -= 1
        print(set_time)

print("time's up")