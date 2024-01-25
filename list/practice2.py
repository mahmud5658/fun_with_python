name = ["Abdullah","Akash","Rakibul","Hasan"]
print(name)
name.append("Mahin")
name.insert(0,"Masud")
print(name)
name1 = ["Amin","Rahul","Rakin"]

name.extend(name1)
print(name)

for i in name:
    print(i)
    
for i in range(len(name)):
    print(name[i])