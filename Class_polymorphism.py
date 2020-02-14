# different object classes can share the same name
class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):                              # !! both Nico and Felix share the same method name called speak.
        return self.name + " says woof!"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

#creating 2 instances one for each class
niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())
# metod 1 iterasiya ile gormek olur polimprfizmi
for pet in [niko,felix]:                                # pet!!  iterating via list of items

    print(type(pet))
    print(type(pet.speak()))  # both class instances share the same method name called speak
    print()
    print(pet.speak())   # however they are different types here main__.Cat' , main__.Dog'

print()

# metod 2 funksiya ile:
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)

pet_speak(felix)

# Method3, abstract base class use
class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):                   # we a raising an error, It's expecting you to inherit the animal class and then overwrite the speak method.
        raise NotImplementedError("Subclass must implement this abstarct method")

# bunlari acsan erroru gorersen
#myanimal = Animal('fred')
#print(myanimal.speak())

class Dog(Animal):

    def speak(self):
        return self.name+ " says woof!"


class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"

fido = Dog("Fido")
isis = Cat("isis")
# different object classes can share the same method name
print(fido.speak())
print(isis.speak())