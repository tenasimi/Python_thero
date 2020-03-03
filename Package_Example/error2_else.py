try:
    # want to attempt this code
    # may have an error
    result = 10 + 87 #we created here an error, then fixed error to run else block withour exept block
    print(result)
except:
    print("hey it looks like you arent adding correctly!")  # bu block ishlemir, cunki error yoxdu try blokunda
                                                            # birbasha else ye kecir
else:
    print("Add went well")
    print(result)
