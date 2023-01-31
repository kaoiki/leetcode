#x = 121
#x = -121
x = 121
#x = -33

# newX = str(abs(x))
# if newX == newX[::-1] and x > 0:
#     # return True\
#     print("Yes")
# else:
#     if x == 0:
#         # return True\
#         print("Yes")
#     else:
#         # return False
#         print("No")

# if str(x) == str(x)[::-1]:
#     print("yes")
# else:
#     print("no")

# if x < 0:
#     print('no')
# else:
#     if x == 0:
#         print('yes')
#     else:
#         if (x%10) == 0:
#             print('no')
#         else:
#             newX = str(x)
#             if newX == newX[::-1]:
#                 print("yes")
#             else:
#                 print("no")

# if x < 0:
#     print('no')
# else:
#     if x == 0:
#         print('yes')
#     else:
#         if (x%10) == 0:
#             print('no')
#         else:
#             newX = str(x)
#             if len(newX)%2==0:
#                 if newX[0:int(len(newX)/2)] == newX[int(len(newX)/2):][::-1]:
#                     print("yes")
#                 else:
#                     print("no")
#             else:
#                 if newX[0:int(len(newX)/2)] == newX[int(len(newX)/2)+1:][::-1]:
#                     print("yes")
#                 else:
#                     print("no")
#             # if newX == newX[::-1]:
#             #     print("yes")
#             # else:
#             #     print("no")

if x<0:
    print("no")
a=str(x)
for i in range(int(len(a)/2)):
    if a[i]!=a[len(a)-1-i]:
        print("no")

print("yes")