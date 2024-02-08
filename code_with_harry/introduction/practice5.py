iceream = "Vanilla" # global variable

def food():
    vegetable = 'Potato' # local variable
    fruit = 'Mango' # local variable
    print(vegetable+' is a local variable')
    print(fruit+' is a local variable')
    print(iceream+' is a global variable')


food()
print(iceream+' is a global Variable')