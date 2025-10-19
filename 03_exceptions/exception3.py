while True:
    try:
        x = int(input("What's x?"))
    except:
        print("x is not an integer")
    else:
        break
        
        
print(f"x is {x}")
