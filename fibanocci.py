number=input("enter a number ")
first=1
second=1
fib=0
print(first)
print(second)
for i in range(1, int(number)):
    fib=int(first)+int(second)
    print(fib)
    first=second
    second=fib

