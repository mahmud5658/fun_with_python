import time

cout_time = 5

for i in reversed(range(cout_time+1)):
    if i>0:
        print(i,end='>>>')
        time.sleep(1)
    else:
        print('start')