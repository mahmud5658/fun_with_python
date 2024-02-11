import time


count_seconds = 10

for i in range(count_seconds+1):
    if i>0:
        print(i,end=">>>")
        time.sleep(1)
    else:
        print('Start')