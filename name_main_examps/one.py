#kogda delaem run  python one.py, to proisxodit sleduyuwee v backgrounde:
#And that allows you to have an IF block to check if they're equal to each other.
#and then they say kind of run a bunch of functions that they find here.
#print('hello')

#if __name__ == "__main__":
#   myfunc()

def func():
    print("FUNC() IN ONE.PY")          #importa gedecey, called full name
    
print("TOP LEVEL IN ONE.PY")         #importa gedecey

if __name__ == "__main__":
    print('ONE.PY is being run directly!')
else:
    print('ONE.PY has been imported!')          #importa gedecey
