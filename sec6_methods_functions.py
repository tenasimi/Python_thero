# ex. of method than built-in in object
mylist = [1, 2, 3]
print(mylist)
mylist.append(4)
print(mylist)

print(mylist.pop())  # vicitaet posledniy element lista

print(mylist)
help(mylist.insert)


def name_of_function():
    print("Hello")


name_of_function()


def name_of_functio_n(name):
    print("Hello " + name)


name_of_functio_n('Ubbe')


def add_function(num1, num2):
    return num1 + num2


result = add_function(10, 90)
print(result)


def name_function():
    '''
    DOCSTRING: Information about this function
    INPUT: poka cto pusto . . .
    OUTPUT: Hey, you must do the best
    '''
    print('Hello')


name_function()
help(name_function)

def say_hello(name='NAME'):  #daem znacenie by default
    print('hello ' + name)

say_hello()

result = say_hello('Thor')
rezult = say_hello('Odin')
print(type(result))   #none type, because is just a  print And because this function is just printing
# something out it's actually not returning anything to assign to a variable

def add(n1,n2):
    return  n1 + n2

summ = add(200,30)
print(summ)



def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False

dog_check('My dog run away')
