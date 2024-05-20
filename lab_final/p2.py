class Animal:

  def __init__(self, name, species, age):
    self.name = name
    self.species = species
    self.age = age
    self._treatments = [] 

  def add_treatment(self, treatment):
    self._treatments.append(treatment)
  def get_treatments(self):
    return self._treatments

  def display_info(self):
    print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}")

class Dog(Animal):

  def __init__(self, name, age, breed):
    super().__init__(name, "Dog", age)
    self.breed = breed

  def display_info(self):
    super().display_info()
    print(f"Breed: {self.breed}")

class Cat(Animal):

  def __init__(self, name, age, fur_color):
    super().__init__(name, "Cat", age)
    self.fur_color = fur_color

  def display_info(self):
    super().display_info()
    print(f"Fur Color: {self.fur_color}")

class Bird(Animal):

  def __init__(self, name, age, species):
    super().__init__(name, "Bird", age)
    self.species = species

  def display_info(self):
    super().display_info()
    print(f"Species: {self.species}")

class Treatment:
  def __init__(self, date, description):
    self.date = date
    self.description = description

  def display_details(self):
    print(f"Date: {self.date}, Description: {self.description}")

def main():
  dog = Dog("Buddy", 3, "Labrador Retriever")
  cat = Cat("Whiskers", 1, "Siamese")
  bird = Bird("Tweety", 2, "Canary")

  dog.add_treatment(Treatment("2024-05-13", "Vaccination"))
  cat.add_treatment(Treatment("2024-05-15", "Hairball removal"))
  bird.add_treatment(Treatment("2024-05-17", "Wing clipping"))

  dog.display_info()
  print("Treatments for Buddy:")
  for treatment in dog.get_treatments():
    treatment.display_details()
  print()
  cat.display_info()
  print("Treatments for Whiskers:")
  for treatment in cat.get_treatments():
    treatment.display_details()
  print()
  bird.display_info()
  print("Treatments for Tweety:")
  for treatment in bird.get_treatments():
    treatment.display_details()

if __name__ == "__main__":
  main()