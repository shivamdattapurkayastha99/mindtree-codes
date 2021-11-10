# given n print 0 to n by identifying whether n is even or odd 
n=int(input())
print("n: ",n)
if n%2==0:
    for i in range(0,n+1,2):
        print(i)


else:
    for i in range(1,n+1,2):
        print(i)