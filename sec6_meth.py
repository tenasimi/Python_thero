def say_hello(name='NAME'):
    print('hello ' + name)

say_hello()
say_hello('Jonny')

print()
###################

def say_hello(name='NAME'):
    return'hello ' + name

result = say_hello('Jose')
print(result)
print(type(result))

def add(n1,n2):
    return  n1 + n2    # return turns func type from none to string

result = add(20,30)
print(result)

#Find out if the word "dog" is in a string?

def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False

dog_check('My dog run away')

print(dog_check('My dog run away'))

def myfunc(a,b):
    # Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05
print(myfunc(10000,7000))
# proizvolniy nomer peremennix mojem peredavat
def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(40,60,100))