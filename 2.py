#      *
#     **
#    ***
for i in range(5):
    for j in range(1,6-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()
    