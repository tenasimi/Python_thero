print(1 % 2)
print(2 % 2)
print(3 % 2)
print(4 % 2)
print(5 % 2)
print(6 % 2)
print(7 % 2)
print(8 % 2)
print(9 % 2)

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)
print(almost_there(190))

print(abs(20-11))

#help(map)
print()
def square(num):
    return num**2

print(square(6))


def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print ("Original String: ", s)
    print("No. of Upper case characters: ", d["upper"])
    print("No. of Lower case characters: ", d["lower"])
#vizivaem
s='Hello mr. Rogers, how are you, this fine Tuesday?'
up_low(s)

print()

def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
l = [1,1,1,1,3,3,4,6,5,6,9,46]

print(unique_list(l))

print()

def multiply(numbers):
    total = numbers[0]
    for x in numbers:
        total *= x
    return total
numbers = [1,2,3,-4]
print(multiply(numbers))

print()

def palindrome(s):
    return s == s[::-1]

print(palindrome('alla'))

print()

import string

def ispangram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
