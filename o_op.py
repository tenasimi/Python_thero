mylist = [1,2,3]    # is a var or object
mylist.append(5)  # dot shows  a bunch of attributes an methods on this object
print(mylist)   # append() takes exactly one argument

myset = set("67")
myset.add(56)                 # these are built-in objects
print(myset)                  # everything in python are objects

print(type(mylist))           # pokajet tip ili klass obyekta
print(type(myset))

#use class keyword to create a user defined object
# for a user defined object a class is a blueprint that defines a nature of a future object
# from classes we can construct an instance of the object

class Sample():        # we created simplest class without attributes
    pass

my_sample = Sample()  #  and instanse of that class

print(type(my_sample))

# creating attributes of class
# spesial init method, called upon when we create an instance of the class
# self keyword connects method to the instance of the class
# self keyword is a reference to the instance of the class
# init metod acts like a constructor

class Dog():

    #class object attribute -> same for any instance of a class
    species = 'mammal'

    def __init__(self,breed,name,spots):    # when creating an instance we must pass an !Arguments
        self.breed = breed       # self.breed eto !Atribut gde = breed eto !Param. name
        self.name = name
        self.spots = spots
        # init is a construction method where self keyword + all attibutes
                    # argument = attributes = parameter names !!! CAN BE THE SAME!!! dlya leqkosti
        # it's just cleaner is to have all three of these

    def bark(self):
        print("WOOF! My name is {}".format(self.name))


my_dog = Dog(breed='Huskie', name='Sharik', spots=False)  # parameter names

print(type(my_dog))  #they you have an instance of dOG Class (ekzemplyar klasa Dog)

var = my_dog.breed
var1 = my_dog.name
var2 = my_dog.spots
var_glob = my_dog.species
print(var)
print(var1)
print(var2)
print(var_glob)
print(my_dog.bark) # vizivaem kak attribut
my_dog.bark()     # vizivaem kak metod



