from typing import Pattern


# Pattern
# input:5
# 1
# 352
# 4$5$6
# 10$9$8$7
# 11$12$13$14$15
c=0
n=int(input())
for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,i+1):
            c+=1
            if j<i:
                print(c,"$",end=" ")
            else:
                print(c)
    else:
        c+=i
        for j in range(j,i+1):
            if i>j:
                print(c,"$",end=" ")
            else:
                print(c,end=" ")
            c-=1
        c+=i
    print()            