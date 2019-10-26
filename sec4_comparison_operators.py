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
