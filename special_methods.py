mylist = [1,2,3]
# len function, print function are special builin python functions
print(len(mylist))

class Sample():
    pass

mysample = Sample()


#len(mysample)
print(mysample)
print(mylist)

class Book():

    def __init__(self,title,author,pages):

        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return  f"{self.title} by {self.author}"      #f string literal format

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")



b = Book('Python rocks','Jose',200)

#del b

print(b)       # will show that its a book object in memory
print(str(b))
print(len(b))

del b

# pokajet cto ohject b udalen -> NameError: name 'b' is not defined
# print(b)
