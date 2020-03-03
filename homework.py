def ask_for_int():
    waiting = True
    while waiting:
     try:
         result=int(input("Please provide number: "))
         x=result**2
         print(x)

     except:                                          # esli est owibka prodoljit sprawivat/srabotaet
         print("Please try again! \nThat is not a number")
         continue
     else:                                   #means is no exception, #birbasha else ye kecir
         waiting = False


ask_for_int()
