#x = 121
x = -121

newX = str(abs(x))
if newX == newX[::-1] and x > 0:
    # return True\
    print("Yes")
else:
    if x == 0:
        # return True\
        print("Yes")
    else:
        # return False
        print("No")