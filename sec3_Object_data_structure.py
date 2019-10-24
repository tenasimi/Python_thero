mystring = "Hello World"
print(mystring)
print(mystring[0])
print(mystring[3])
print(mystring[-1])  # reverse indexing
print(mystring[-3])
print(mystring[3:])  #all the way to the end
print(mystring[:5])  # from beginning
print(mystring[2:8]) # up to
print(mystring[::])  # default step size 1
print(mystring[::2]) # with step size 2
print(mystring[2:9:2]) # from to with step 2
print(mystring[::-1]) # reverses string
print()
name = "Sam"
last_letters = name[1:]
print(last_letters)
print('P' + last_letters) #concatenation ex.
letter = 'z'
print(letter * 10) #multiplication ex.
x = "Hello World"
print(len(x))
print(x.upper()) # metod upper
print(type(name))
print(x.split())
y='hi this is a string'
print(y.split())
print(y.split("i")) #udalyaet by default split will split on the whitespace but it could actually split it on any letter I want.
print()
print('This is a string {}'.format('INSERTED'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {1} {0} {2}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
print('The {f} {q} {k}'.format(f='fox', q='brown', k='quick'))
print('The {f} {f} {f}'.format(f='fox', q='brown', k='quick'))
print()
result = 100/777
print(result)
#we can change the level of precision we want and even change the width of the number itself
print("The result was {}".format(result))
print("The result was {r}".format(r=result))
# Float formatting follows "{value:width.precision f}"
print("The result was {r:1.3f}".format(r=result))  #okruglili
print("The result was {r:10.5f}".format(r=result))
print()
name = "Nasimi"
print('Hello, his name is {}'.format(name))
print(f'Hello, his name is {name}')      #f string method
age = 3
print(f'{name} is {age} years old.')
print()
# indexing, slicing and concatenation of lists
my_list = ['STRING',100, 23.2]
print(len(my_list))
mylist = ['one','two','three']
print(mylist[0])
print(mylist[1:])
another_list = ['four','five']
print(mylist + another_list)
new_list = mylist + another_list
print(new_list)
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('six')
print(new_list)
new_list.append('seven')  # adding to list
print(new_list)
new_list.pop()   # removing from end of list
print(new_list)
popped_item = new_list.pop()
print(popped_item)
print(new_list)
new_list.pop(0)  # remove selected item, first
print(new_list)
new_list = ['a','e', 'x','b', 'c']
num_list = [4,1,8,3]
print(new_list)
new_list.sort() # metod sortirovki
print(new_list)
# none-type ex.
my_sorted_list = new_list.sort()
print(my_sorted_list)  # vivedet tip none
print(type(my_sorted_list))
print(num_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
print()
#dictionary ex.
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key2'])
prices_lookup = {'apple':2.99, ''
                               'oranges':1.99, 'milk':5.80}
print(prices_lookup['apple'])
print()
d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}}
print(d['k2'])
print(d['k3'])
print(d['k3']['insideKey']) #viziv iz vstroennoy dict  key # dict
print(d['k2'][2]) # grab 2 from list, What I need to do is say d k 2 which returns back the list and then I want the item index too.
print()
# dict has a key1 and associate if this key is a list of lower case letters ABC
dict = {'key1': ['a','b','c']}
print(dict)
mylist =dict['key1']
print(mylist)
letter = mylist[2]
print(letter)
print(letter.upper()) # teper eto vse sdelaem v odnoy strocke:
# to je samoe polucili:
print(dict['key1'][2].upper())
print()
# add new key to dict
dic={'k1': 100, 'k2': 200}
print(dic)
dic['k3'] = 300
print(dic)
dic['k1'] = 'NEW VALUE'
print(dic)
# posmotret vse keys i values i items
print(dic.keys())
print(dic.values())
print(dic.items())
print()
t=(1,2,3)
mylist = [1,2,3]
print(type(t),type(mylist))
print(len(t),len(mylist))
print()
t = ('one', 2)
print(t[0],t[-1])
# counting how many times appears an item
t =('a', 'a', 'b')
print(t.count('a'))
# s kakoy pozisii nacinaetsa
print(t.index('a'))
print()
myset = set()
print(myset)
myset.add(1)
print(myset)
myset.add(2)
print(myset)
# vibiraem s setom tolko unique znaceniya iz list-a:
mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3]
print(mylist)
print(set(mylist))

print(set('Mississipi'))

print(type(False))
print(1>2)
print(type(True))
print(1==1)
print(1<=1)
print(1>1)
# data type None:
b = None
print(b)
myfile = open('myfile.txt')  # funksiya open
myfile.seek(0)    # cursor reset
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()
with open('myfile.txt') as my_new_file:   # created var ssilayuwiysa na myfile.txt
    contents = my_new_file.read()         # assigned that var to contents, imenovali
print(contents)             #napecatali, tut bez close mojem oboditsa
print()
with open('myfile.txt',mode='r') as my_new_file:
    contents = my_new_file.read()
print(contents)
print()
# read mode
with open('my_new_file.txt',mode='r') as f:
    print(f.read())
# append mode, dobavka k suwestvuyuwemu
with open('my_new_file.txt',mode='a') as f:
    f.write('\nFOUR ON FOURTH')
with open('my_new_file.txt',mode='r') as f:
    print(f.read())
# write mode, if a file not exists, creates new file. Overrides existing file!!
with open('selfcreated.txt', mode='w') as f:
    f.write('I  CREATED THIS FILE')
# citaem eqo teper
with open('selfcreated.txt',mode='r') as f:
    print(f.read())