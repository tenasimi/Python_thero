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