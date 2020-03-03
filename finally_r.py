try:
    f=open('testfile','r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
#except OSError:   #konkret de vere bilersen err tipini
    #print('Hey you have an OS Error')
except:                                   # umumi de vere bilersen
    print('All other exceptions')
finally:
    print("I always run")