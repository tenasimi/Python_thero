print(1 < 2 and 2 > 3)
print(1 < 2 and 2 < 3)
print('h' == 'h' and 2 == 2) # AND!! both of them must be true
print(1 == 2 or 2 < 3) # OR!! one of them must be true
print(not 1 == 1) # NOT !! for opposite boolean result
#
if True:
    print('ITS TRUE!')
#
if False:
    print('ITS False!')
else:
    print('Its always True')
#
if 3>2:
    print('3 greater 2, TRUE')
else:
    print('3 is not greater 2, False')
#
if 3<2:
    print('3 greater 2, TRUE')
else:
    print('3 is not greater 2, False')
#
hungry = True
if hungry:
    print('FEED ME!')

#
hungry = True
if hungry:
    print('FEED ME!') #empty output
else:
    print('Im not hungry')

#
loc = 'Bank'
if loc == 'Auto Shop':
    print('Cars are cool!')
else:
    print('I do not know much, maybe its bank')

#for checking other conditions use ELIF
# we can add and more lives for more conditions.
loc = 'Bank'
#loc = 'Auto Shop'
loc = 'Store'
if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!')
else:
    print('I do not know much')

#
#name = 'Jose' # esli nicto ne podoydet
#name = 'Frankie'
name = 'Sammy'
if name == 'Frankie':
    print('Hello Frankie!')
elif name == 'Sammy':
    print('Hello Sammy')
else:
    print('What is your name?')

# for loop
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)
print()
#
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)
#

mylist = [1,2,3,4,5,6,7,8,9,10]
for jelly in mylist:
    print(jelly)

#


mylist = [1,2,3,4,5,6,7,8,9,10]
for jelly in mylist:
    print('hello')

#
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    # check for even
    if num % 2 ==0:
        print(num)

print()

# snacala iz spiska otbiraem cetnie cisla (if), a potom (else) vivodin to cto ostalos (necetnie)
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num % 2 == 0:          # to cto delitsa na 2 bez ostatka
        print(num)
    else:
        print(f'Odd Number: {num}')

print()

# to je samoe, naoborot, cnacala necetnie, potom to cto ostalos - cetnie
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num % 2 == 1:        # to cto delitsa na 2 s ostatkom 1
        print(num)
    else:
        print(f'Even Number: {num}')

print()
#
mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num   #0+1=1, 1+2=3, 3+3=6, 6+4=10, 10+5=15,15+6=21,21+7=28,28+8=36,36+9=45,45+10=55
print(list_sum)
print()
#
mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num   # to je samoe no podrobno v stolbike uvidim process slojeniya
    print(list_sum)             # placing print inside of for loop
print()
#
# iterating letters i string:
mystring = 'Hello World'
for letter in mystring:
    print(letter)
print()
# ex. Print cool for as many times as your characters in string
for ggg in 'Hello World':
    print('Cool!')

# You can also use the same iteration for each tuple.
# pecataem cto xotim v cislo raz soderjimoqo tu;ipa
tup = (1,2,3)
for item in tup:
    print('cislo raz')
#
print()
# pecataem soderjanie tulip-a
tup = (1,2,3)
for item in tup:
    print('item')

print()
#
mylist = [(1,2),(3,4),(5,6),(7,8)]
print(len(mylist))
for item in mylist:
    print(item)

#unpack tuple ex.
print()

mylist = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in mylist:
    print(a)
    print(b)

#unpack tuple ex.
print()

mylist = [(1,2),(3,4),(5,6),(7,8)]
for a,b in mylist:
    print(b)

#unpack tuple ex .
print()

mylist = [(1,2,3),(5,6,7),(8,9,10)]
for item in mylist:
    print(item)


print()
# But I can do tuple unpacking here, only print 2 6 9 ex.:
mylist = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in mylist:
    print(b)

print()
# Dictionary iteration
#by default when you iterate through a dictionary you only iterate through the Keys.
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)

print()
# if you want iterate through items themselves call .items(:
d = {'k1':1, 'k2':2, 'k3':3}
for item in d.items():
    print(item)

print()
# primenyaya priem visheprivedenniy v tuple, mojno delat UNPACKING
d = {'k1':1, 'k2':2, 'k3':3}
for key,value in d.items():
    print(value)

print()
# only value ex.
d = {'k1':1, 'k2':2, 'k3':3}
for value in d.values():
    print(value)

print()
# WHILE loop ex.
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1  #or x +=1  is more compact

print()
# WHILE + else
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('X is NOT less than 5')

print()
# pass keyword ex.
x = [1,2,3]
for item in x:
    #  many times programmers keep it as a placeholder to kind of avoid a syntax error b
    pass
print('end of my script')

#
print()

mystring = 'Sammy'
for letter in mystring:
    print(letter)

# I'm not actually printing out the letter.
print()
mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

# break ex. - stopping loop.
print()
mystring = 'Samrikitmo'
for letter in mystring:
    if letter == 'k':
        break
    print(letter)

# break ex. - stopping loop at 2.
print()

x = 0
while x < 5:
    if x == 2:  # dobavlyaem
        break   # break uslovie
    print(x)
    x += 1
#
print()
#mylist = [a,b,c]
for bam in range(3):  #all range from 0 to 3
    print(bam)

print()
#mylist = [a,b,c]
for num in range(2,5):  #start from 2 not include 5
    print(num)

print()
#mylist = [a,b,c]
for num in range(3,10,2):  #start from 3 not include 5 + step size 2
    print(num)

k = list(range(3,28,2))
print(k)

print()
# enumerate with format + for
index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

print()
# to je samoe no s funksiey enumerate
word = 'abcde'
for item in enumerate(word):  # v enumerate stavim iterable var - word
    print(item)

print()
# delaem enumerate + tuple unpacking
word = 'abcde'
for ind,let in enumerate(word):  # znaya cto vivedet tuple, delaem unpack naxodu
    print(ind)
    print(let)
    print('\n')

# zip - funksiya sozdayuwaya tuple iz listov
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for item in zip(mylist1,mylist2):
    print(item)

print()
# zip - funksiya sozdayuwaya tuple iz listov
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

print()
# zip - Zipp is only going to be able to go and zip together as far as the list which is the  shortest.
mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

print()
#list + zip - zipping together 2 lists
l = list(zip(mylist1,mylist2))
print(l)

# in
# in keyword  PROVERKA USLOVIYA, est li x v spiske?
# is X in the list 1 to 3 and 0 return back a boolean true or false.
print('x' in ['x','y','z'])
print()
print('a' in 'a world')   # string ex
print()
print('mykey' in {'mykey':345})  # dict ex.
print()
d={'mykey':345}
print(345 in d.keys())
print(345 in d.values())
print()
# min  max functions
mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

# random library use
from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)  # peremewivaet (shuffle)
print(mylist)

print()

# ramdom integer function , grabs random int from interval
from random import randint
print(randint(0,100))

# also i can save its random output and use later
mynum = randint(0,10)
print(mynum)
#
# input
print(input('Enter a number here: '))

result = input('What is your name?  ')
print(result)

print(type(result))

result = input('What is your favorite number?  ')

print(float(result))

print(int(result))
