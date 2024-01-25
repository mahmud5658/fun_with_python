age = 24
text = "This is Abdullah Al Mahmud.My age is:",+age

print(text)

name = "My name is Abdullah Al Mahmud\nand I am {}"
print(name.format(age))

quantity = 3
itemNo = 5658
price = 56

order = "I want {} \\pieces\\ of item {} for {} \'dollars\'"
print(order.format(quantity,itemNo,price))