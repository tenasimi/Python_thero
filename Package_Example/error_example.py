def add(n1,n2):
    print(n1+n2)

add(10,20)

number1 = 10
number2 = input("Please provide a number: ")


#add(number1,int(number2))  doljno bit tak, a to vivedet error
add(number1,number2)    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("Something happened!")

# error verecek, buna gore bu kodu try blokunun icine saliriq ki error vermesin ve davam etsin
# error2.py fayla bax