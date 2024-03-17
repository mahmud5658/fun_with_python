x = "Awesome"

def func():
    global x
    x = "Fantastic"
    print('Python is '+x)
    
    
func()
print('Python is '+x)