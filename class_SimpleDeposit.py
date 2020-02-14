class Simple:

    def __init__(self,value):
        self.value=value

    def add_to_value(self,amount):
        self.value=self.value+amount
        print(('We just added {} to your value'.format(amount)))

myObj=Simple(300)
print(myObj.value)
myObj.add_to_value(50)      #nicego ne daet, no + delaet
print(myObj.value)          #pri sleduyuwem vizove
myObj.add_to_value(50)
print(myObj.value)