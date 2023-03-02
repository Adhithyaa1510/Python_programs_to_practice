number=input("Enter a number ")
i=2
flag=0
for i in range(2,int(int(number)/2)+1):
    if (int(number)%i)==0:
        flag=1
if(flag==1):
    print("It is not a prime")
else:
    print("it is a prime")
