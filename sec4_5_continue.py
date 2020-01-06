mystring = 'hello nasimi'
mylist= []
for letter in mystring:
    mylist.append(letter)
print(mylist)

#
print()
# to je samoe no koroce, For i in v liste!!!

mystring = 'developer'
newlist = [letter for letter in mystring]
print(newlist)

#ex2
print()

mylist = [x for x in range(0,11)]
print(mylist)

mylist = [num**2 for num in range(0,11)]
print(mylist)
#grab even numbers
mylist = [x for x in range(0,11) if x%2==0]
print(mylist)
# square of even numbers
mylist = [x**2 for x in range(0,11) if x%2==0]
print(mylist)

# celcius to fahrenheit
celcius = [0,10,20,34.5]
fahrenheit = [( (9/5)*temp +32 ) for temp in celcius]
print(fahrenheit)

# to je samoe, no s .append
fahrenheit = []
for temp in celcius:
    fahrenheit.append((9/5)*temp +32 )
print(fahrenheit)

print()
#using if - else in list comprehension
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

print()
#nested loop ex.

mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)  #mojem slaqat ili umnojat list1 na kajdiy element lista 2
print(mylist)

print()
#nested loop ex2.

mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)  #kajdiy elem list1 na kajdiy list2
print(mylist)
print(help(mylist.append))
print()
#nested loop ex. to je samoe no pokoroce :

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)

print()
#statements assestment test
st = 'Print only the words that start with s in this sentence'
print(st.split())
for word in st.split():
    print(word)

#
print()
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)

# if we have a capital S i xotim ctobi toje vivodilsa
print()
st = 'Sam Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':  #ili tak -> if word[0]== 's' or word[0]=='S'
        print(word)

#ex. print all even nums in range 0 - 10
print()
print(list(range(0,11,2)))
for num in range(0,11,2):
    print(num)

print()
#ex. create a list of all nums between 1 and 50 that are divisible by 3
print([x for x in range(1,51) if x%3 == 0])

print()
#ex. print every word in this sentence that has an even number of letters
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word+ ' >> is even!')

print()
#ex. print integers from 1 to 100, but for multiples of three print "Fizz"
#instead of the num, and for the multiples of five  print "Buzz"
#for numbers kotorie delyatsa na 3 i 5 oba print FizzBuzz
for num in range(1,101):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else:
        print(num)

print()
#ex create a list of the first letters of every word in this string
st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])

print(help(mylist.index))


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['veggie']))
    else:
        print('I did not find any fruit here')


myfunc(fruit='apple', veggie='lettuce')