class Circle():
    # class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi
        #One thing to consider is that if you have an attribute it doesn't necessarily have t
        # o be defined from a particular parameter call.


    # method
    def get_circumference(self):
        return self.radius * self.pi * 2  # dlina okrujnosti
        #return self.radius * Circle.pi * 2 -> toje same self.pi = Circle.pi

# create instance of the circle
my_circle = Circle()  # ne peredaem argument, tak kak est defaut radius=1

print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())

my_circle = Circle(30) #default rad. will be overwritten
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)
