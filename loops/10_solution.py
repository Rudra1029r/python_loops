import time

wait_time = 1
max_try = 5
attempt = 0

while attempt < max_try:
    print("Attempt",attempt +1,"-wait time",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempt +=1