class Dog():


    # class object attribute
    # same for any instance of class
    species = 'mammal'

    def __init__(self,breed,name):

        # let create Attributes of an instance with init constructor method
        # we take in the argument (self+)
        # assign it using self.attribute_name = param. name
        self.breed = breed
        self.name = name

    # Operations/Actions ---> Methods
    def bark(self, number):
        print("WOOF! My name is {} and the number is {} ".format(self.name, number))
        # it gets connected to the object via the use o self keyword

#create instance of the dog
my_dog = Dog('Lab', 'Frankie')

var0 = type(my_dog)
var1 = my_dog.name
var2 = my_dog.species
var3 = my_dog.bark  #call as attribute -> hey you have this metod thats bound on your object dog

print("-------------------------")
print(var0," * * *  ",var1," * * *  ",var2," * * *",var3)
print("-------------------------")
my_dog.bark(8)   #call as method (action that the actual object can take)



