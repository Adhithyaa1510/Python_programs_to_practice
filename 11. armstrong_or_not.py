number=input("enter the number ")
list=[int(x) for x in str(number)]
print(list)
i=0
armstrong=0
for i in range(0,len(list)):
    res=pow(int(list[i]),int(len(list)))
    armstrong=armstrong+res
print(armstrong)
if (armstrong==int(number)):
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")