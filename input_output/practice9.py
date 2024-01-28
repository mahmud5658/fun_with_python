a = 25
b = 7
c = 2003

print(a,b,c,sep="-")

import io

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)

# get the value from dummy file
print(dummy_file.getvalue())



print("This is Abdullah Al Mahmud. Daffodil International University.",file=open('abd.txt'))
