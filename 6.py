# lucky number  
# sum of first half digits=sum of second half digits
# no of digits should be even
n=int(input())
sum1=0
sum2=0
for i in range(len(str(n))//2):
    sum1+=int(str(n)[i])
for i in range(len(str(n))//2,len(str(n))):
    sum2+=int(str(n)[i])
if sum1==sum2:
    print("YES")
else:
    print("NO")
