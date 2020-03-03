def ask_for_int():
    while True:
     try:
         result=int(input("Please provide number: "))
     except:                                          # esli est owibka prodoljit sprawivat/srabotaet
         print("Whoops! That is not a number")
         continue
     else:                                   #means is no exception
         print("Yes thank you")
         break
     finally:
         print("End of try/except/finally")
         print("I will always run at the end!")

ask_for_int()
