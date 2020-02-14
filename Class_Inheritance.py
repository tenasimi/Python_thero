class Animal():

    def __init__(self):
         print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am animal")

    def eat(self):
        print("I am eating")

myanimal = Animal() #__init__ method gets automatically executed when you
                       # create Anumal()

myanimal.who_am_i()
myanimal.eat()
print()

#Dog is a Derived class from the base class Animal
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print("WOOF!")

    def eat(self):
        print("I am a dog and eating")

mydog = Dog()
mydog.eat()
mydog.who_am_i()
mydog.bark()
mydog.eat()