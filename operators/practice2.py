x = "Awesome"
def func():
    global x
    x = 'Fantastic'
    print("Python is awesome: "+x)

func()
print("Python is: "+x)
