def ask_for_int():
    try:
        result=int(input("Please provide number: "))
    except:
        print("Whoops! That is not a number")
    finally:
        print("End of try/except/finally")

ask_for_int()
