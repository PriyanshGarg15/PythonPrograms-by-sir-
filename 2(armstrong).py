n=int(input("enter no.="))
n1=n
c=0
sum=0
while(n1>0):
    c=c+1
    n1=n1//10
n1=n
while (n1>0):
        r = n1 % 10
        sum = sum + r**c
        n1 = n1 // 10
print(sum)
if(sum==n):
    print("armstrong")
else:
    print("not armstrong")
