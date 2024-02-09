for i in range(10):
    print(i,end=' ')
    
print()

i = 0
while i<10:
    if i==6:
        i+=1
        continue
    else:
        print(i,end=' ')
    i+=1