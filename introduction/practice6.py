#  declare a variable and initialize
x = 100

# global variable in function

def func():
    global x
    print(x)
    # modifying the global variale
    x ="Abdullah Al Mahmud"
    print(x)
# Calling function

func()
print(x)