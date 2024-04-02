class Dog:
    # class attribute
    attribute = "Mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


dog1 = Dog("Jonny")
dog2 = Dog("Tommy")

print("{} is a {}".format(dog1.name, dog1.__class__.attribute))
print("{} is a {}".format(dog2.name, dog2.__class__.attribute))

dog1.speak()
dog2.speak()
