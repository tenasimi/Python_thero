mystring = 'hello'
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