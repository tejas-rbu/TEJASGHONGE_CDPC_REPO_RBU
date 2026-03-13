n=int(input("enter n:"))
x=int(input("enter x:"))
sum=1
for i in range(1,n):
    sum=sum+(x**i)/i;
print(sum)